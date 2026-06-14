# 사이트 공통 설정
BASE_URL = "https://gunpo-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# IndexNow 키 (빙·네이버·얀덱스 즉시 색인 통보). 빌드 시 루트에 <KEY>.txt 키파일 생성.
INDEXNOW_KEY = "9ab48d34df28a1cc39f9cbd7fdda6bb1"

# 대표 행정동 10곳 (slug, 한글명) — 내부링크·메뉴 공용
# 번호 행정동(군포1·2동→군포동, 산본1·2동→산본동)은 대표 동으로 통합한다.
AREAS = [
    ("gunpo-dong-chuljangmassage", "군포동"),
    ("sanbon-dong-chuljangmassage", "산본동"),
    ("geumjeong-dong-chuljangmassage", "금정동"),
    ("jaegung-dong-chuljangmassage", "재궁동"),
    ("ogeum-dong-chuljangmassage", "오금동"),
    ("suri-dong-chuljangmassage", "수리동"),
    ("gungnae-dong-chuljangmassage", "궁내동"),
    ("gwangjeong-dong-chuljangmassage", "광정동"),
    ("daeya-dong-chuljangmassage", "대야동"),
    ("songbu-dong-chuljangmassage", "송부동"),
]

# 지하철역세권 6곳 (slug, 한글명) — 1·4호선 환승 금정역 등
STATIONS = [
    ("geumjeong-station-chuljangmassage", "금정역"),
    ("sanbon-station-chuljangmassage", "산본역"),
    ("surisan-station-chuljangmassage", "수리산역"),
    ("daeyami-station-chuljangmassage", "대야미역"),
    ("gunpo-station-chuljangmassage", "군포역"),
    ("dangjeong-station-chuljangmassage", "당정역"),
]


def area_url(slug):
    return f"/gunpo/{slug}/"


def station_url(slug):
    return f"/gunpo/{slug}/"


# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("출장마사지 안내", "/#service", [
        ("서비스 안내", "/#service"),
        ("전지역 방문 가능", "/#coverage"),
        ("예약 전 확인 기준", "/#check"),
        ("홈타이 이용 가이드", "/hometai-guide/"),
    ]),
    ("지역별 안내", "/#areas", [
        (name, area_url(slug)) for slug, name in AREAS
    ]),
    ("지하철역별 안내", "/#stations", [
        (name, station_url(slug)) for slug, name in STATIONS
    ]),
    ("예약안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("방문 가능 지역", "/reservation/#place"),
        ("결제·이동비 안내", "/reservation/#payment"),
        ("변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/precautions/", [
        ("방문 전 준비", "/precautions/#prepare"),
        ("지역별 이동 기준", "/precautions/#outer"),
        ("위생·안전 기준", "/precautions/#hygiene"),
        ("자주 묻는 질문", "/precautions/#faq"),
    ]),
    ("고객센터", "/support/", [
        ("공지사항", "/support/#notice"),
        ("자주 묻는 질문", "/support/#faq"),
        ("1:1 문의", "/support/#contact"),
        ("개인정보처리방침", "/privacy/"),
    ]),
]
