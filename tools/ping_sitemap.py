#!/usr/bin/env python3
"""사이트맵 핑 (레거시) — 참고용.

중요: 구글은 2023년 6월, 빙은 그 이전에 익명 sitemap ping 엔드포인트
(/ping?sitemap=...)를 폐지했습니다. 네이버도 공개 핑 엔드포인트가 없습니다.
따라서 사이트맵 핑은 더 이상 색인을 보장하지 않습니다.

가장 빠른 색인 경로는 다음과 같습니다(권장 순서):
  1) IndexNow  → tools/indexnow.py   (빙·네이버·얀덱스 즉시 통보)
  2) 구글      → tools/google_indexing.py (Indexing API) 또는 서치콘솔 사이트맵 제출
  3) 서치콘솔/서치어드바이저에서 sitemap.xml·rss.xml 1회 등록(자동 재수집)

이 스크립트는 호환을 위해 레거시 핑을 시도하되, 실패는 정상입니다.
"""
import os
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

SITEMAP = f"{BASE_URL.rstrip('/')}/sitemap.xml"
# 폐지되었을 수 있는 레거시 엔드포인트(참고용)
LEGACY = [
    "https://www.google.com/ping?sitemap=",
    "https://www.bing.com/ping?sitemap=",
]


def main() -> None:
    enc = urllib.parse.quote(SITEMAP, safe="")
    print(f"사이트맵: {SITEMAP}\n")
    for base in LEGACY:
        url = base + enc
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                print(f"  HTTP {resp.status}  {base}")
        except Exception as e:  # noqa: BLE001
            print(f"  (폐지/실패-정상)  {base}  → {e}")
    print("\n→ 즉시 색인은 tools/indexnow.py / tools/google_indexing.py 를 사용하세요.")


if __name__ == "__main__":
    main()
