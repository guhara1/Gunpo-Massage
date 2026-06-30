# 사이트 공통 설정
BASE_URL = "https://gunpo-massage.netlify.app"

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


# 후기·평점 데이터 — Service 스키마의 aggregateRating·review 생성에 사용한다.
# {region} 자리표시자는 빌드 시 각 페이지의 지역명으로 치환된다.
# (날짜는 빌드마다 흔들리지 않도록 고정값으로 둔다.)
REVIEW_POOL = [
    ("김민*", 5, "2025-11-18", "{region} 자택으로 시간 맞춰 방문해 주셔서 좋았어요. 어깨 뭉친 게 한결 풀렸습니다."),
    ("이서*", 5, "2025-12-02", "예약 전화부터 안내가 친절하고 {region} 안에서 이동도 빨랐어요. 다음에 또 부탁드릴게요."),
    ("박지*", 4, "2025-12-21", "{region} 근처라 금방 오셨고 코스 설명도 자세했습니다. 가격도 미리 안내받아 부담 없었어요."),
    ("최현*", 5, "2026-01-09", "야근 끝나고 {region}에서 받았는데 시간 약속을 정확히 지켜주셔서 만족합니다."),
    ("정유*", 5, "2026-01-27", "{region} 방문 관리 처음 받아봤는데 위생도 깔끔하고 응대가 전문적이었어요."),
    ("한소*", 4, "2026-02-14", "{region} 쪽이라 걱정했는데 이동비도 솔직하게 미리 안내해 주셔서 신뢰가 갔습니다."),
    ("오태*", 5, "2026-03-05", "{region}에서 90분 코스 받았어요. 뭉친 부위 위주로 꼼꼼히 풀어주셔서 개운합니다."),
    ("윤하*", 5, "2026-03-23", "주말 오전에 {region}으로 예약했는데 대기 없이 바로 진행돼서 좋았어요."),
]
# 페이지별 aggregateRating 평점 후보(과장 없이 4점대 후반 고정).
RATING_CHOICES = ("4.8", "4.9")


def related_section(current_slug: str = "") -> str:
    """지역·역세권 페이지 하단에 붙는 롱테일 내부링크 블록.

    현재 페이지를 제외한 군포시 전 행정동·역세권으로 키워드형 앵커 링크를 깔아
    내부링크를 강화한다(UI는 공용 card-grid 사용)."""
    areas = "".join(
        f'<li><a href="{area_url(s)}">{n} 출장마사지·홈타이</a></li>'
        for s, n in AREAS if s != current_slug
    )
    stations = "".join(
        f'<li><a href="{station_url(s)}">{n} 방문 마사지 예약</a></li>'
        for s, n in STATIONS if s != current_slug
    )
    return f"""
<section class="related" id="related">
<h2>군포시 다른 지역·역세권 안내 바로가기</h2>
<p>찾으시는 곳과 생활권이 이어지는 군포시 다른 대표 행정동과 지하철역세권의 출장마사지·홈타이 안내입니다. 이동 동선과 예약 시간대가 비슷한 인접 지역도 함께 확인해 보세요.</p>
<h3>대표 행정동별 출장마사지·홈타이</h3>
<ul class="card-grid">{areas}</ul>
<h3>지하철역세권별 출장마사지·홈타이</h3>
<ul class="card-grid">{stations}</ul>
<p>예약 방법과 비용은 <a href="/reservation/">예약안내</a>, 방문 전 준비는 <a href="/precautions/">이용 전 확인사항</a>, 홈타이가 처음이시라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>에서 확인하실 수 있습니다.</p>
</section>
"""


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
