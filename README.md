# 간다GO — 군포 출장마사지·홈타이 지역 SEO 사이트

경기도 군포시에서 방문형 마사지(출장마사지)·홈타이를 찾는 사용자가
본인 위치에 맞는 지역 정보를 쉽게 확인할 수 있도록 만든 정적 지역 SEO 사이트입니다.
군포시는 행정구가 없으므로 **군포시 → 대표 행정동 → 지하철역** 순서로 구조를 잡습니다.

- **상호:** 간다GO
- **예약전화:** 0508-202-4719
- **핵심 키워드:** 출장마사지 / **보조:** 홈타이
- **지역 키워드:** 군포 출장마사지, 군포시 출장마사지, 군포 홈타이

## 구조 (총 22페이지)

```
메인 1
대표 행정동 10   (군포동·산본동·금정동·재궁동·오금동·
                  수리동·궁내동·광정동·대야동·송부동)
지하철역세권 6   (금정역·산본역·수리산역·대야미역·군포역·당정역)
안내 페이지 5    (예약안내·이용 전 확인사항·홈타이 이용 가이드·
                  개인정보처리방침·고객센터)
```

번호 행정동(군포1·2동→군포동, 산본1·2동→산본동)은 개별 페이지를 만들지 않고
대표 동으로 통합합니다. 금정역은 1호선·4호선 환승역이지만 노선·방향별로
페이지를 나누지 않고 1개 페이지로만 운영합니다.

## URL 규칙

| 구분 | 경로 |
|------|------|
| 메인 | `/` |
| 대표 행정동 | `/gunpo/<slug>-chuljangmassage/` |
| 역세권 | `/gunpo/<station>-station-chuljangmassage/` |

> 메인페이지는 배포 도메인 루트(`/`)에 위치합니다. 워드프레스 슬러그
> `/gunpo-chuljangmassage/`로 운영하려면 해당 경로로 리다이렉트하세요.

## 빌드

```bash
python3 build.py
```

`content/` 패키지의 페이지 정의를 읽어 각 경로에 `index.html`을 생성하고
`sitemap.xml`, `robots.txt`, `.nojekyll`을 갱신합니다.

- 본문 텍스트 2,000자 미만 페이지는 자동으로 `noindex` 처리됩니다.
- 모든 페이지에 `WebPage`·`BreadcrumbList` 구조화 데이터가 자동 삽입되고,
  메인에는 `Organization`·`FAQPage`가 추가됩니다.
- 오프라인 매장 주소가 없으므로 `LocalBusiness` 스키마는 사용하지 않습니다.

## 배포 전 설정

- `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경한 뒤 `python3 build.py` 재실행.

## 색인(인덱싱) 최속화

`python3 build.py` 실행 시 다음 색인 자산이 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | `lastmod`·`changefreq`·`priority` 포함 (색인 신선도 신호) |
| `rss.xml` | 네이버 서치어드바이저 RSS 수집·빠른 색인용 |
| `robots.txt` | 전체 허용 + Yeti(네이버)·Googlebot·bingbot 명시, sitemap·rss 링크 |
| `<INDEXNOW_KEY>.txt` | IndexNow 소유 증명 키파일(루트 게시) |

메인페이지 `<head>`에 RSS·sitemap `<link>`와 네이버 인증 메타태그가 들어갑니다.

### 1) IndexNow — 빙·네이버·얀덱스 즉시 통보 (시크릿 불필요)

키는 `content/site.py`의 `INDEXNOW_KEY`. 사이트에 키파일이 게시되어 있으면 즉시 동작.

```bash
python3 tools/indexnow.py                         # 사이트맵 전체 제출
python3 tools/indexnow.py https://gunpo-massage.pages.dev/gunpo/sanbon-dong-chuljangmassage/  # 특정 글
```

### 2) 구글 Indexing API — 구글 즉시 통보 (서비스 계정 필요)

구글은 IndexNow 미참여. 최초 1회 설정:
1. Google Cloud → **Indexing API** 사용 설정 → 서비스 계정 JSON 키 발급
2. **서치콘솔**에서 서비스 계정 이메일을 사이트 **소유자**로 추가
3. `pip install google-auth requests`

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python3 tools/google_indexing.py
```

### 3) GitHub Actions 자동화 — 글 올릴 때마다 자동 통보

`.github/workflows/indexing.yml` 이 `main`/`master` 푸시(콘텐츠 변경) 시 빌드 후
IndexNow를 자동 제출합니다. 구글까지 자동화하려면 리포지토리 시크릿
`GOOGLE_SERVICE_ACCOUNT` 에 서비스 계정 JSON 전체를 넣으세요.
Cloudflare Pages 프로덕션 브랜치에 맞춰 워크플로의 `branches` 를 조정하세요.

> 참고: 구글·빙의 익명 `sitemap ping` 엔드포인트는 폐지되었습니다(`tools/ping_sitemap.py`
> 는 참고용). 빠른 색인은 IndexNow + Indexing API + 서치콘솔/서치어드바이저
> 사이트맵 1회 등록 조합이 가장 효과적입니다.

### 최초 수동 등록 (1회)

- **네이버 서치어드바이저**: 사이트 등록 → `sitemap.xml`·`rss.xml` 제출 (메인 메타태그로 소유확인 완료됨)
- **구글 서치콘솔**: 속성 추가 → `sitemap.xml` 제출
- **빙 웹마스터도구**: 사이트 추가 → 사이트맵 제출 (이후 IndexNow 자동)

## 디렉터리

```
build.py            빌드 스크립트(HTML·sitemap·rss·robots·IndexNow 키파일 생성)
content/            페이지 정의 (site, main, areas, stations, info, pricing)
assets/             style.css, nav.js, 파비콘/OG 이미지
tools/              indexnow.py · google_indexing.py · ping_sitemap.py
.github/workflows/  indexing.yml (푸시 시 색인 자동 통보)
```
