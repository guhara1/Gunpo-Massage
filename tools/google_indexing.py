#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 스크립트.

구글은 IndexNow에 참여하지 않으므로, 구글에 즉시 색인을 알리려면
Indexing API(urlNotifications:publish)를 사용한다.

준비 (최초 1회):
  1) Google Cloud 콘솔에서 프로젝트 생성 → "Indexing API" 사용 설정.
  2) 서비스 계정 생성 → JSON 키 다운로드.
  3) 구글 서치콘솔에서 해당 사이트(gunpo-massage.netlify.app)의
     "소유자"로 서비스 계정 이메일(...@....iam.gserviceaccount.com)을 추가.
  4) 의존 패키지 설치:  pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json

  # 사이트맵의 모든 URL 통보
  python3 tools/google_indexing.py

  # 특정 URL만 통보
  python3 tools/google_indexing.py https://gunpo-massage.netlify.app/gunpo/sanbon-dong-chuljangmassage/

참고: 공식적으로 Indexing API는 JobPosting·BroadcastEvent 구조화 페이지를
권장 대상으로 안내합니다. 일반 페이지 제출은 정책을 확인한 뒤 사용하세요.
일일 호출 쿼터(기본 200건)가 있습니다.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def session():
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존 패키지가 필요합니다:  pip install google-auth requests")
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 "
                 "JSON 키 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    return AuthorizedSession(creds)


def publish(urls: list) -> None:
    sess = session()
    ok = 0
    for u in urls:
        resp = sess.post(ENDPOINT, json={"url": u, "type": "URL_UPDATED"})
        if resp.status_code == 200:
            ok += 1
            print(f"  OK   {u}")
        else:
            print(f"  FAIL {resp.status_code} {u} :: {resp.text[:200]}")
    print(f"\n구글 색인 통보 완료: {ok}/{len(urls)}건 성공")


if __name__ == "__main__":
    publish(sys.argv[1:] or sitemap_urls())
