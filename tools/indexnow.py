#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 스크립트.

IndexNow 단일 엔드포인트(api.indexnow.org)에 URL을 제출하면 참여 검색엔진
(Bing, Naver, Yandex, Seznam, Yep 등)에 동시에 색인 요청이 전달된다.
구글은 IndexNow에 참여하지 않으므로 tools/google_indexing.py 를 사용한다.

사용법:
  # 사이트맵의 모든 URL 제출(기본)
  python3 tools/indexnow.py

  # 특정 URL만 제출(글 새로 올렸을 때)
  python3 tools/indexnow.py https://gunpo-massage.netlify.app/gunpo/sanbon-dong-chuljangmassage/

표준 라이브러리만 사용한다(외부 패키지 불필요).
"""
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def host_of(url: str) -> str:
    return re.sub(r"^https?://", "", url).split("/")[0]


def sitemap_urls() -> list:
    """로컬 sitemap.xml에서 URL 목록을 읽는다."""
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def submit(urls: list) -> None:
    host = host_of(BASE_URL)
    payload = {
        "host": host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow 제출 → {host} ({len(urls)}건)")
    for u in urls:
        print("  ", u)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"\n응답: HTTP {resp.status} {resp.reason}")
            # 200/202 = 정상 접수. 422 = 키/URL 불일치, 403 = 키파일 검증 실패.
    except urllib.error.HTTPError as e:
        print(f"\nHTTP {e.code}: {e.read().decode('utf-8', 'ignore')}")
        if e.code in (403, 422):
            print("키 파일이 사이트에 게시되어 있는지 확인하세요: "
                  f"{BASE_URL.rstrip('/')}/{INDEXNOW_KEY}.txt")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"제출 실패: {e}")


if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    submit(urls)
