import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="Python for Chinese Text Preprocessing",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================================================================
# 🎛️ [사용자 스타일 설정 블록 (STYLE_CONFIG)]
# 폰트 크기(px 단위)와 줄간격/여백을 이곳에서 자유롭고 직관적으로 미세조정하세요!
# ==============================================================================
STYLE_CONFIG = {
    # 1. 최상단 메인 제목 & 소제목
    "page_title_size": "50px",  # 메인 제목 크기 ("🐍 Python for Chinese Text Preprocessing")
    "page_title_line_height": "1.6",  # 메인 제목 줄간격 (상단 잘림 방지용 여유 공간)
    "page_subtitle_size": "25px",  # 메인 소제목 크기 ("경희대학교 중어중문 전공생들을 위한...")
    "page_subtitle_line_height": "1.6",  # 메인 소제목 줄간격
    # 2. 세션 및 섹션 제목
    "intro_title_size": "30px",  # [ Introduction ] 제목 크기
    "intro_title_margin_top": "28px",  # [ Introduction ] 위쪽 간격 (텍스트 한 줄 분량 여백)
    "section_title_size": "30px",  # 3열 대단원 제목 ("📑 영상 목차", "🎬 강의 시청", "📥 실습 파일 및 링크")
    "section_title_weight": "800",  # 3열 대단원 제목 굵기 (700: 보통 굵게, 800: 아주 굵게, 900: 초강력 굵게)
    "card_title_size": "20px",  # 우측 카드 소제목 ("⚙️ 사전준비 안내", "☁️ 실습파일 링크", "📚 언어분석자료")
    # 3. 본문 텍스트 (상단 소개글 및 전체 본문 단락 내용)
    "body_font_size": "17px",  # 전체 본문 및 소개글 글자 크기
    "body_line_height": "1.75",  # 전체 본문 및 소개글 줄간격
    # 4. 버튼 및 설명문(캡션)
    "button_font_size": "15px",  # 좌측 목차 및 우측 링크 버튼 글자 크기
    "caption_font_size": "12px",  # 회색 보조 설명문 글자 크기
}

# ==============================================================================
# [전역 스타일 엔진] 사용자 설정값을 최상위 우선순위(!important)로 확실하게 주입
# ==============================================================================
st.html(f"""
<style>
    /* 상하단 레이아웃 여백: 상단 잘림 방지를 위해 padding-top을 넉넉히 확보 */
    .block-container {{
        padding-top: 3rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }}
    
    /* 1. 최상단 메인 제목: 상단 잘림 방지 패딩 및 전용 폰트 */
    .hero-title {{
        font-size: {STYLE_CONFIG["page_title_size"]} !important;
        line-height: {STYLE_CONFIG["page_title_line_height"]} !important;
        font-weight: 800 !important;
        text-align: center !important;
        padding-top: 0.5rem !important;
        margin-bottom: 0.4rem !important;
        overflow: visible !important;
    }}
    
    /* 2. 최상단 소제목 */
    .hero-subtitle {{
        font-size: {STYLE_CONFIG["page_subtitle_size"]} !important;
        line-height: {STYLE_CONFIG["page_subtitle_line_height"]} !important;
        font-weight: 600 !important;
        color: #111111 !important;
        text-align: center !important;
        margin-top: 0 !important;
        margin-bottom: 1.5rem !important;
    }}

    /* 3. [ Introduction ] 전용 제목 */
    .intro-header {{
        font-size: {STYLE_CONFIG["intro_title_size"]} !important;
        font-weight: 700 !important;
        color: #111111 !important;
        margin-top: {STYLE_CONFIG["intro_title_margin_top"]} !important;
        margin-bottom: 0.8rem !important;
        line-height: 1.4 !important;
    }}

    /* 4. 소개글 상자 본문 문단 (body_font_size 통합 적용) */
    .intro-paragraph {{
        font-size: {STYLE_CONFIG["body_font_size"]} !important;
        line-height: {STYLE_CONFIG["body_line_height"]} !important;
        margin-bottom: 0.8rem !important;
        word-break: keep-all !important;
    }}

    /* 5. 3열 세션 대제목 (##, ###) - 선택자 완화 및 초강력 굵기(900 + 외곽선 보강) 적용 */
    h2, h3,
    .stMarkdown h2, .stMarkdown h3,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3 {{
        font-size: {STYLE_CONFIG["section_title_size"]} !important;
        font-weight: {STYLE_CONFIG["section_title_weight"]} !important;
        -webkit-text-stroke: 0.3px currentColor !important;
        margin-top: 0.4rem !important;
        margin-bottom: 0.6rem !important;
        line-height: 1.4 !important;
    }}

    /* ##, ### 내부의 모든 텍스트 및 볼드(**) 태그도 초강력 굵기 강제 적용 */
    h2 *, h3 *,
    .stMarkdown h2 *, .stMarkdown h3 *,
    div[data-testid="stMarkdownContainer"] h2 *,
    div[data-testid="stMarkdownContainer"] h3 * {{
        font-weight: 900 !important;
        -webkit-text-stroke: 0.3px currentColor !important;
    }}

    /* 6. 우측 카드 및 토글(Expander) 소제목 */
    div[data-testid="stMarkdownContainer"] > h4,
    [data-testid="stExpander"] details summary,
    [data-testid="stExpander"] details summary p,
    [data-testid="stExpander"] details summary span {{
        font-size: {STYLE_CONFIG["card_title_size"]} !important;
        font-weight: 600 !important;
        margin-top: 0.2rem !important;
        margin-bottom: 0.4rem !important;
        line-height: 1.4 !important;
    }}
    
    /* 7. 일반 본문 단락 (p, li) */
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li {{
        font-size: {STYLE_CONFIG["body_font_size"]} !important;
        line-height: {STYLE_CONFIG["body_line_height"]} !important;
        word-break: keep-all !important;
        overflow-wrap: break-word !important;
    }}

    /* 8. 보조 설명문/캡션 */
    .stCaption, [data-testid="stCaptionContainer"],
    [data-testid="stCaptionContainer"] p {{
        font-size: {STYLE_CONFIG["caption_font_size"]} !important;
        line-height: 1.45 !important;
    }}
    
    /* 9. 좌측 목차 버튼 */
    button[kind="secondary"], button[kind="primary"],
    button[kind="secondary"] p, button[kind="primary"] p {{
        white-space: normal !important;
        word-break: keep-all !important;
        text-align: left !important;
        font-size: {STYLE_CONFIG["button_font_size"]} !important;
        padding: 0.4rem 0.65rem !important;
        line-height: 1.35 !important;
        height: auto !important;
    }}

    /* 10. 우측 링크 버튼 */
    a[kind="secondaryFormSubmit"], a[data-testid="stLinkButton"],
    a[data-testid="stLinkButton"] p {{
        white-space: normal !important;
        word-break: keep-all !important;
        text-align: center !important;
        font-size: {STYLE_CONFIG["button_font_size"]} !important;
        line-height: 1.35 !important;
    }}
</style>
""")

# ==============================================================================
# 2. 강의 영상 데이터 (총 40개 강좌 전체 및 주제별 그룹화)
# ==============================================================================
LECTURE_GROUPS = {
    "Part 1. 파이썬 기초 문법 (숫자형 & 문자열)": [
        ("1. 숫자형_사칙연산_round_짝수홀수", "fpWsSKmPuxQ"),
        ("2-1. 문자열_oneline_multiline_연산_정렬", "7m2i-nupBPk"),
        ("2-2. 문자열_len_indexing_count_idex_find_slicing", "6kQBpzOgzwc"),
        ("3. 문자열_formating_escape_lower_upper_title_split", "CSMzMCuJNKM"),
        ("4. 문자열_join_replace_strip_rstrip_lstrip", "X9RahQdHJNk"),
    ],
    "Part 2. 컬렉션 자료형 (리스트 & 사전형)": [
        ("5-1. 리스트_indexing_slicing_수정", "5F5poMJcMMA"),
        ("5-2. 리스트_append_del_insert_remove_sorted_sort_reverse", "rOBkx6u2FWw"),
        ("6-1. 사전형_key_value_keys_values_items", "i8CFlmN63GY"),
        ("6-2. 사전형_del_clear_중국어사전", "Z6AEFIjBp6s"),
        ("7. 사전형_문자열formating_input_operator_itemgetter", "Bq0BXxTEmMU"),
    ],
    "Part 3. 제어문 (반복문 for)": [
        ("8. 반복문for_range_for문중첩_구구단", "4wOJpYAAPqY"),
        ("9-1. 반복문for_사진붙이기_문자열formating_숫자증가", "RXpvRKcBgNk"),
        (
            "9-2. 반복문for_가위바위보_input_list_random_sample_문자열formating",
            "-P_fzy3jaSg",
        ),
        ("9-3. 반복문for_range_if_elif_count", "lzrEii5XQaY"),
        ("9-4. 반복문for_if_elif_count_문자열formating", "GToDr7HQAr4"),
    ],
    "Part 4. 어휘 빈도 분석 (Dictionary & Operator)": [
        ("10-1. 어휘빈도_list_dictionary_for_if_elif", "3sxP2emET8Y"),
        ("10-2. 어휘빈도_list_dictionary_for_if_elif", "7OKAJeLtMp0"),
        ("10-3. 어휘빈도_list_dictionary_for_if_elif", "xb7QZjIb0z8"),
        ("11-1. 어휘빈도_operator_sorted_itemgetter_tuple", "NBSesICszLQ"),
        ("11-2. 어휘빈도_operator_sorted_itemgetter_tuple", "qlnQSga3dKc"),
        ("11-3. 어휘빈도_with open_for_dictionary_fwrite_txt", "V_ZBeqY_MFk"),
    ],
    "Part 5. 시스템 및 파일 입출력 (os & open)": [
        ("12. 위치확인_drive_os_getcwd_chdir_listdir", "doi3S8GuSG4"),
        ("13-1. 파일입출력_pwd_open_txt_w_close", "93DWHiXq94w"),
        ("13-2. 파일입출력_open_w_a_r_slash n_txt", "xjacI1Bma0Q"),
        ("14-1. 파일입출력_with open_r_read_readline_readlines", "SL9wwEQbeRc"),
        ("14-2. 파일입출력_with open_w_a_r_codecs", "6krI0fznJ9A"),
    ],
    "Part 6. 정규표현식 (Regular Expression: re)": [
        ("15. 정규표현_corpus_re_match_search_findall", "fLsC9e_QuXI"),
        ("16-1. 정규표현_re_meta character", "7ZaL-JdoUx0"),
        ("16-2. 정규표현_re_greedy_non greedy", "ivaONVxiq5A"),
        ("17-1. 정규표현_re_split", "_NnS8eUrVyw"),
        ("17-2. 정규표현_re_sub", "RyGSrGeoWLw"),
    ],
    "Part 7. 실전 중국어 텍스트 전처리 (Colab & Corpus)": [
        ("18. 실전_google colab_files_drive", "4w8amOKFufg"),
        ("19. 실전_os_chdir_listdir_with open_read_re_split_sub", "zqmJUUgOyuM"),
        ("20. 실전_len_re_split_for_range_count", "CiOx-55_ugc"),
        ("21. 실전_for_문자열formating_re_sub_split_len_1", "eSsBv5iVzjw"),
        ("22-1. 실전_불용어처리_stopwords_hit_scu_if_not_in", "t2dbujhFZCM"),
        ("22-2. 실전_불용어처리_stopwords_hit_scu_if_not_in", "zeR4ta2biv4"),
        ("23. 실전_어휘빈도_dictionary_list_sorted_operator_itemgetter", "nu9_Su7Da5Y"),
        ("24-1. 실전_파일저장_txt_csv_chart", "--rsovxII64"),
        ("24-2. 실전_파일저장_txt_csv_chart", "mzcNpR9dBp0"),
    ],
}

# 빠른 검색 및 조회를 위한 매핑 딕셔너리
FLAT_VIDEOS = {}
for group_name, vlist in LECTURE_GROUPS.items():
    for title, vid in vlist:
        FLAT_VIDEOS[title] = {
            "group": group_name,
            "url": f"https://www.youtube.com/watch?v={vid}",
            "vid": vid,
        }

# 세션 상태 초기화 (현재 선택된 영상)
if "selected_video_title" not in st.session_state:
    st.session_state["selected_video_title"] = "1. 숫자형_사칙연산_round_짝수홀수"

# ==============================================================================
# [헤더 영역] 제목 및 원문 내용 (마크다운 들여쓰기 오류 원천 방지)
# ==============================================================================
st.html("""
<div>
    <h1 class="hero-title">🐍 Python for Chinese Text Preprocessing</h1>
    <h3 class="hero-subtitle">경희대학교 중어중문 전공생들을 위한 중국어 텍스트 전처리 강의</h3>
</div>
""")

with st.container(border=True):
    st.html("""
<div>
    <p class="intro-paragraph">
        <span style="color: #1a73e8; font-weight: bold;">경희대학교 중어중문 전공생</span>들을 위해 Python for Chinese Text Preprocessing 강의를 공유합니다. 링크된 강의는 "중국어디지털리터러시(2023)"의 일부로서 <span style="color: #1a73e8; font-weight: bold;">중국어를 Python으로 어떻게 다루는지</span> 궁금한 전공생들을 위해 공개합니다. 바이브(Vibe)코딩의 유행에도 불구하고 <span style="color: #1a73e8; font-weight: bold;">텍스트코딩은 여전히 중요</span>합니다. 강의는 <span style="color: #1a73e8; font-weight: bold;">중국어문을 전공함에도 코딩이라는 허들로 인해 접근을 망설인</span>, 그럼에도 시대 트렌드에 따라 한 번은 배워봐야 하진 않을까 생각해온 <span style="color: #1a73e8; font-weight: bold;">"찐 인문계-문과생-중문인"</span>을 대상으로 하고 있습니다. 그럼에도 이해가 어려운 부분이 있다면 어느 파이썬 책을 찾아도 관련 개념들이 나오니 각자의 환경에서 나름의 탐색을 개진해봐도 좋겠습니다.
    </p>
    
    <h2 class="intro-header">[ Introduction ]</h2>
    
    <p class="intro-paragraph">
        중국어문 학습의 목적은 <span style="color: #1a73e8; font-weight: bold;">원어민과의 원활한 의사소통</span>에 있습니다. 마찬가지로, 기계어 학습의 목적은 <span style="color: #1a73e8; font-weight: bold;">컴퓨터와의 원활한 지시와 소통</span>에 있습니다. 하지만 거기서 멈추면 안 됩니다. 이제는 중국어가 빅데이터의 모습으로 존재하기 때문입니다. 우리는 빅데이터로서의 중국어, 그 속의 <span style="color: #1a73e8; font-weight: bold;">숨은 의미를 파악하기 위해 텍스트 처리 능력이 필요</span>합니다. 이제는 "중국어를 잘 하는 능력" 뿐만 아니라, 중국어를 "잘 처리하는 능력" 역시 필요한 시대입니다. Python이란 기계어로 중국어 텍스트 처리를 할 줄 알아야 하는 이유입니다. 중국어 전공자는 누구보다 그것을 잘 해야 합니다. 겁내지 마세요. 초보 수준의 Python 문법으로도 중국어 텍스트를 다룰 수 있습니다. <span style="color: #1a73e8; font-weight: bold;">"제3의 외국어로서 기계어"이란 관점에서 Python을 학습</span>하세요. 그리고 이 역시도 "외국어"인만큼 중국어 만큼의 꾸준한 연습이 필요합니다.
    </p>
</div>
""")

st.write("")  # 미세 간격 조정

# ==============================================================================
# [본문 3열 구성 레이아웃]
# 왼쪽: 영상의 목차 | 중간: 영상 플레이어 | 오른쪽: 실습 파일 및 링크
# ==============================================================================
col_left, col_mid, col_right = st.columns([1.1, 2.1, 1.1], gap="medium")

# ------------------------------------------------------------------------------
# 1. 왼쪽 열: 영상의 목차
# ------------------------------------------------------------------------------
with col_left:
    st.markdown("## [ 📑 영상 목차 ]")

    # 강의 검색창
    search_query = st.text_input(
        "🔍 강의 검색",
        "",
        placeholder="예: 문자열, 어휘빈도, 정규표현",
        label_visibility="collapsed",
    )

    if search_query.strip():
        # 검색 필터링 모드
        matched = [t for t in FLAT_VIDEOS if search_query.strip().lower() in t.lower()]
        st.caption(f"검색 결과: {len(matched)}개")
        if matched:
            for t in matched:
                is_active = t == st.session_state["selected_video_title"]
                btn_type = "primary" if is_active else "secondary"
                if st.button(
                    f"{'🔴' if is_active else '▶️'} {t}",
                    key=f"s_btn_{t}",
                    type=btn_type,
                ):
                    st.session_state["selected_video_title"] = t
                    st.rerun()
        else:
            st.info("검색어와 일치하는 강의가 없습니다.")
    else:
        # 파트별 아코디언 토글 목차
        current_title = st.session_state["selected_video_title"]
        current_group = FLAT_VIDEOS.get(current_title, {}).get("group", "")

        for group_name, vlist in LECTURE_GROUPS.items():
            is_expanded = group_name == current_group
            with st.expander(f"📁 {group_name}", expanded=is_expanded):
                for title, vid in vlist:
                    is_active = title == current_title
                    btn_type = "primary" if is_active else "secondary"
                    icon = "🔴" if is_active else "▶️"
                    if st.button(f"{icon} {title}", key=f"btn_{title}", type=btn_type):
                        st.session_state["selected_video_title"] = title
                        st.rerun()

# ------------------------------------------------------------------------------
# 2. 중간 열: 영상 구동 창
# ------------------------------------------------------------------------------
with col_mid:
    selected_title = st.session_state["selected_video_title"]
    selected_info = FLAT_VIDEOS[selected_title]
    video_url = selected_info["url"]
    group_name = selected_info["group"]

    st.markdown("## [ 🎬 강의 시청 ]")

    with st.container(border=True):
        st.markdown(f"#### 📌 {selected_title}")
        st.caption(
            f"소속 파트: **{group_name}** | YouTube ID: `{selected_info['vid']}`"
        )

        # YouTube 비디오 재생
        st.video(video_url)

        st.markdown("---")
        btn_c1, btn_c2 = st.columns([1, 1])
        with btn_c1:
            st.link_button("🌐 YouTube 바로가기", video_url)
        with btn_c2:
            st.html(
                f"""
            <div style="display: flex; justify-content: flex-end; width: 100%;">
                <a href="https://sites.google.com/view/pythonforchinesetextpreprocess/home" target="_blank"
                   style="display: inline-flex; align-items: center; justify-content: center;
                          padding: 0.45rem 0.85rem; font-size: {STYLE_CONFIG['button_font_size']};
                          text-decoration: none; border-radius: 0.5rem;
                          border: 1px solid rgba(128, 128, 128, 0.35); background-color: transparent;
                          color: inherit; font-weight: 500; line-height: 1.35; cursor: pointer;">
                    🔗 원문 사이트 바로가기
                </a>
            </div>
            """
            )

# ------------------------------------------------------------------------------
# 3. 오른쪽 열: 파일 링크 및 리소스
# ------------------------------------------------------------------------------
with col_right:
    st.markdown("## [ 📥 실습 파일 및 링크 ]")

    # [1] 사전준비 안내 (토글)
    with st.expander("⚙️ 사전준비 안내", expanded=False):
        st.caption("실습 전 Google Colab 설치 필요")
        st.link_button(
            "🚀 Google Colab 설치하기",
            "https://workspace.google.com/u/0/marketplace/app/colaboratory/1014160490159?flow_type=2",
        )
        st.link_button(
            "📺 설치 방법 영상 확인",
            "https://youtu.be/vRu77RmGD-M?si=tMYUvf6R9NjoU9nf",
        )

    # [2] 실습파일 링크(Google Colab) (토글)
    with st.expander("☁️ 실습파일 링크 (Google Colab)", expanded=True):
        st.caption("클릭 후 '파일' → '드라이브에 사본 저장' 후 실습하세요.")
        st.link_button(
            "1. python(int_float_string_list_dic)",
            "https://drive.google.com/file/d/1Fe3pkW-MtkwQ_5YSMB5BOcAuH3BOy0zV/view?usp=sharing",
        )
        st.link_button(
            "2. python(for_loop)",
            "https://drive.google.com/file/d/1x0cr_a6HkvIoKImwecCfOC4vXAJUOry4/view?usp=sharing",
        )
        st.link_button(
            "3. python(input_output_regex)",
            "https://drive.google.com/file/d/1XX85BXUhhzu_ousnWgPuESYFXqJyW_sg/view?usp=sharing",
        )
        st.link_button(
            "4. Python(text_preprocessing_stopword)",
            "https://drive.google.com/file/d/1s5AXXpLEWsGuHAizBjARHCI-fue3S8VZ/view?usp=sharing",
        )

    # [3] 언어분석자료 (토글)
    with st.expander("📚 언어분석자료", expanded=False):
        st.caption("중국 역대 지도자 新年賀詞(신년사) 연설문 및 불용어 사전(Stopwords)")
        st.link_button(
            "1. 江澤民 (1994, 1995년 연설)",
            "https://drive.google.com/file/d/1VplkeJDqmihTc7S4xWQanOwxDGa_lDcD/view?usp=drive_link",
        )
        st.link_button(
            "2. 胡錦濤 (2004, 2005년 연설)",
            "https://drive.google.com/file/d/1b9HgRWMroIlh0uMmXC0_BY6ydMdHSX-x/view?usp=drive_link",
        )
        st.link_button(
            "3. 習近平 (2014, 2015년 연설)",
            "https://drive.google.com/file/d/165peumoP8jpYg4I7eaQzHoJBrJWmcKYr/view?usp=drive_link",
        )
        st.link_button(
            "🔤 stopword (HIT) - 하얼빈공대",
            "https://drive.google.com/file/d/1UG9ZECPvSacaHB2L6apb44qUPRhO8PfZ/view?usp=drive_link",
        )
        st.link_button(
            "🔤 stopword (SCU) - 쓰촨대",
            "https://drive.google.com/file/d/1w-0jfLsMENocEc_EEzV0Ch5BnyggPUOV/view?usp=drive_link",
        )
