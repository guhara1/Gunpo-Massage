# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import (AREAS, BASE_URL, BRAND, PHONE, PHONE_DISPLAY, STATIONS,
                   area_url, station_url)
from .pricing import PRICING

_AREA_CARDS = "".join(
    f'<li><a href="{area_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in AREAS
)
_STATION_CARDS = "".join(
    f'<li><a href="{station_url(slug)}">{name} 출장마사지</a></li>'
    for slug, name in STATIONS
)

_JSONLD = f"""<meta name="naver-site-verification" content="afb3727220fa34049d082286412ec45de75baf89">
<meta name="naver-site-verification" content="bc297c8b5e8e2e84de1f339818b42d83056030b2" />
<link rel="preload" as="image" href="/assets/hero.webp" type="image/webp" fetchpriority="high">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "경기도 군포시 전지역 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 군포시"
  }}
}}
</script>
"""
# 참고: FAQPage 구조화 데이터는 build.py가 본문의 .faq-item 블록에서 자동 생성한다.
# (메인뿐 아니라 모든 페이지에 동일 규칙으로 적용 — 수기 중복 정의를 제거함)

_HERO = f"""<section class="hero">
  <div class="hero-inner hero-grid">
    <div class="hero-text">
      <p class="hero-badge">Premium Visiting Spa · 경기도 군포시 전지역</p>
      <h1>군포 출장마사지·군포시 홈타이<br>지역별 예약 안내</h1>
      <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>군포시 대표 행정동과 역세권 어디든 전화 한 통이면 예약이 끝납니다.</p>
      <div class="hero-actions">
        <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
        <a class="hero-btn" href="#areas">지역별 안내 보기</a>
      </div>
      <ul class="hero-stats">
        <li><strong>10곳</strong><span>대표 행정동</span></li>
        <li><strong>6개</strong><span>지하철역세권</span></li>
        <li><strong>전지역</strong><span>방문 가능</span></li>
        <li><strong>24시간</strong><span>예약 상담</span></li>
      </ul>
    </div>
    <div class="hero-media">
      <picture>
        <source srcset="/assets/hero.webp" type="image/webp">
        <img src="/assets/hero.jpg" alt="군포 출장마사지·군포시 홈타이 방문 관리 안내" width="1200" height="675" fetchpriority="high" decoding="async">
      </picture>
    </div>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>군포시에서 출장마사지를 찾는 이유</h2>
<p>군포 출장마사지를 찾는 분들은 대부분 지금 계신 곳에서 가까운 방문 가능 지역을 먼저 확인합니다. 군포시는 산본신도시 생활권, 금정역 환승권, 군포역·당정역 생활권, 대야미역 주변 주거권이 한 도시 안에 함께 있는 곳입니다. 산본동과 광정동은 중심 상권과 아파트 단지 수요가 많고, 금정동은 1호선과 4호선이 만나는 환승 생활권입니다. 군포동은 당동·당정동·부곡동 생활권을 함께 고려해야 하며, 대야동과 송부동은 차량 이동 기준이 중요한 지역입니다. {BRAND}는 예약 확인부터 방문 관리까지 정해진 절차에 따라 진행하며, 이 페이지는 군포시 전체 구조를 설명하는 허브 역할을 합니다. 더 자세한 내용은 대표 행정동 페이지와 지하철역세권 페이지에서 확인하실 수 있습니다.</p>
<p>군포시는 행정구가 따로 없는 도시여서, 이 사이트는 군포시 → 대표 행정동 → 지하철역 순서로 구조를 잡습니다. 본문과 제목에는 군포 출장마사지, 군포시 출장마사지, 군포 홈타이 표현을 자연스럽게 함께 사용합니다.</p>
</section>

<section id="coverage">
<h2>군포 홈타이 이용 전 확인할 사항</h2>
<p>군포 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 군포시는 행정구가 없는 만큼, 이 사이트는 메인 아래에 바로 대표 행정동 페이지를 배치합니다. 군포동, 산본동, 금정동, 재궁동, 오금동, 수리동, 궁내동, 광정동, 대야동, 송부동을 각각 대표 지역으로 두고, 페이지마다 생활권과 이동 기준을 다르게 설명합니다. 번호가 붙은 행정동은 개별 페이지로 만들지 않습니다. 군포1동과 군포2동은 군포동으로, 산본1동과 산본2동은 산본동으로 통합해 중복 콘텐츠 위험을 줄였습니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 군포시 대표 행정동 10곳을 기준으로 구성됩니다. 각 페이지에서는 해당 생활권의 특징, 가까운 지하철역, 방문 전 확인사항, 예약 가능 시간, 추가 이동비 여부를 지역마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 지역을 선택해 주세요.</p>
<ul class="card-grid">
{_AREA_CARDS}
</ul>
<p>산본동·광정동은 산본 중심 상권과 아파트 단지 생활권을, 금정동은 1·4호선 금정역 환승권을, 군포동은 군포역·당정역과 당동·부곡동 생활권을, 대야동·송부동은 대야미역 주변과 차량 이동 외곽 주거권을 중심으로 안내합니다.</p>
</section>

<section id="stations">
<h2>금정역·산본역·군포역 역세권 안내</h2>
<p>지하철역별 안내는 군포시를 지나는 지하철역세권을 기준으로 구성합니다. 각 역 페이지에서는 주변 행정동, 이동 동선, 이용 시간대, 예약 전 확인사항을 역마다 다르게 설명하며, 역 이름만 바꾼 반복 페이지나 노선·방향별 중복 페이지는 만들지 않습니다. 특히 금정역은 1호선과 4호선이 만나는 환승역이지만 노선별로 페이지를 나누지 않고 한 페이지에서 함께 안내합니다.</p>
<ul class="card-grid">
{_STATION_CARDS}
</ul>
<p>금정역은 1·4호선 환승권과, 산본역은 산본 중심 상권과, 수리산역은 수리동·궁내동 생활권과, 대야미역은 대야동 주거권과, 군포역은 군포동 중심 생활권과, 당정역은 당정동·부곡동 인근과 연결됩니다.</p>
</section>

<section id="check">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해야 합니다. 군포시는 도시 면적이 크지는 않지만 산본 중심권, 금정 환승권, 군포역 생활권, 대야미 외곽 주거권의 이동 동선이 서로 다를 수 있습니다. 특히 대야동과 송부동은 차량 이동 기준 안내가 중요하므로, 자세한 준비 방법은 <a href="/precautions/">이용 전 확인사항</a>에서, 예약 절차와 결제·이동비 안내는 <a href="/reservation/">예약안내</a>에서 확인해 주세요. 홈타이가 처음이라면 <a href="/hometai-guide/">홈타이 이용 가이드</a>를 함께 보시면 도움이 됩니다.</p>
</section>

<section id="guide">
<h2>군포 출장마사지 사이트 이용 가이드</h2>
<p>메인페이지는 군포시 전체 안내를 담당하고, 대표 행정동 페이지는 세부 지역 검색을, 지하철역세권 페이지는 금정역·산본역·수리산역·대야미역·군포역·당정역 검색 의도를 담당합니다. 거주 지역이 익숙하면 행정동 페이지를, 역 기준 위치가 익숙하면 역세권 페이지를 보시면 됩니다. 어느 페이지를 보셔도 예약 절차와 비용 기준은 동일하며, 최종 안내는 언제나 정확한 주소를 기준으로 이루어집니다. 과장된 표현이나 허위 후기, 불법·선정적인 안내는 사용하지 않으며, 이용 가능 지역과 예약 절차, 취소 기준, 개인정보 처리 기준을 분명하게 보여드리는 것을 원칙으로 합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>군포시 전지역 방문이 가능한가요?</h3>
<p>대표 행정동 10곳과 지하철역세권 6곳을 기준으로 군포시 전지역을 안내합니다. 대야동·송부동처럼 차량 이동이 기준이 되는 외곽 주거권도 방문 가능하며, 예약 시 가능 여부를 확인해 드립니다.</p>
</div>
<div class="faq-item">
<h3>군포1동·산본1동처럼 번호 동은 왜 페이지가 없나요?</h3>
<p>군포1·2동은 군포동, 산본1·2동은 산본동 대표 페이지에서 통합 안내합니다. 같은 생활권을 나눠 반복 설명하지 않기 위해서입니다.</p>
</div>
<div class="faq-item">
<h3>금정역은 환승역인데 노선별 페이지가 따로 있나요?</h3>
<p>금정역 페이지는 1개만 운영합니다. 1호선·4호선 노선별이나 방향별로 페이지를 나누지 않고, 환승역 특징과 주변 생활권을 한 페이지에서 함께 안내합니다.</p>
</div>
<div class="faq-item">
<h3>외곽 주거권은 추가 이동비가 붙나요?</h3>
<p>대야동, 송부동처럼 차량 이동 거리가 있는 지역은 추가 이동비가 발생할 수 있습니다. 예약 시 총비용으로 먼저 안내해 드리며, 산본동·금정동 등 도심 생활권은 대부분 기본 요금으로 안내됩니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>군포 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "군포 출장마사지｜군포시 홈타이 지역별 예약 안내",
    "desc": "군포 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "군포 출장마사지 · 군포시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
