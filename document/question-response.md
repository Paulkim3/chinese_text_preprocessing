# Git, GitHub, Streamlit 배포 및 보안 설정 Q&A 가이드

본 문서는 파이썬 프로젝트(`chinese_text_preprocessing`)를 로컬 Git으로 관리하고, GitHub에 안전하게 탑재(Push)하며, 저장소를 Public으로 전환할 때의 보안 조치 및 Streamlit Community Cloud로 배포하는 전체 과정을 '질문-대답(Q&A)' 형식으로 정리한 가이드입니다.

---

## 1. Git의 첫 Commit 하기

### Q1. `git init`을 하려면 해당 폴더에 직접 들어가서 해야 하나요?
**A.** **네, 반드시 버전 관리를 시작할 프로젝트 폴더로 이동한 뒤 실행해야 합니다.**  
* `git init`을 실행하면 해당 위치에 `.git`이라는 숨김 폴더가 생성되며, 그 폴더를 기준으로 하위의 모든 파일 변경 내역을 추적합니다.
* 홈 디렉토리(`~`)나 엉뚱한 상위 폴더에서 실행하면 컴퓨터 안의 의도치 않은 모든 파일이 깃 추적 대상이 될 수 있으므로 주의해야 합니다.

```bash
# 올바른 방법: 프로젝트 폴더로 먼저 이동 후 초기화
cd /Users/chinesedh/Documents/textpreprocessing
git init
```

---

### Q2. 실수로 홈 디렉토리(루트)에서 `git init`을 했다면 기존 작업이 초기화되나요?
**A.** **아닙니다. 기존 작업 파일이 삭제되거나 초기화되지 않습니다.**  
* 단지 홈 디렉토리(`/Users/chinesedh/`)에 `.git` 폴더가 생겨 홈 전체가 깃 저장소로 인식된 상태일 뿐입니다.
* 아래 명령어로 홈 디렉토리에 생긴 `.git` 폴더만 안전하게 삭제해 주면 원상 복구됩니다:

```bash
rm -rf ~/.git
```

---

### Q3. `rm -rf ~/.git` 실행 후 삭제되었는지는 어떻게 확인하나요?
**A.** 아래 두 가지 방법으로 확인할 수 있습니다:
1. **깃 상태 확인 명령어**:
   ```bash
   git status
   ```
   * 출력 결과: `fatal: not a git repository (or any of the parent directories): .git` 문구가 뜨면 완전히 삭제된 것입니다.
2. **숨김 파일 목록 조회**:
   ```bash
   ls -la ~ | grep .git
   ```
   * 아무 결과도 출력되지 않으면 정상 삭제된 것입니다.

---

### Q4. 첫 커밋(Initial Commit)을 만드는 전체 절차는 어떻게 되나요?
**A.** 프로젝트 폴더에서 아래 순서대로 실행합니다:

```bash
# 1. 프로젝트 폴더 이동
cd /Users/chinesedh/Documents/textpreprocessing

# 2. 깃 저장소 초기화
git init

# 3. 모든 작업 파일을 스테이징 영역에 등록
git add .

# 4. 첫 커밋 생성
git commit -m "첫 번째 커밋: 중국어 텍스트 전처리 프로젝트"
```

---

### Q5. `error: pathspec '...' did not match any file(s) known to git` 에러는 왜 발생하나요?
**A.** **`git commit` 명령어에서 커밋 메시지 옵션인 `-m`을 빠뜨렸기 때문입니다.**
* 예: `git commit "배포용 requirements.txt 추가"` 로 실행한 경우
* Git은 `-m`이 없으면 따옴표 안의 문장을 커밋 메시지가 아니라 **"커밋할 특정 파일 경로(pathspec)"** 로 인식합니다.
* 따라서 `"배포용 requirements.txt 추가"`라는 이름의 파일을 찾으려다 해당 파일이 없어 에러가 발생합니다.
* **해결법**: 반드시 `-m` 옵션을 붙여서 실행합니다.
  ```bash
  git commit -m "배포용 requirements.txt 추가"
  ```

---

## 2. 그 결과물 GitHub로 탑재(Push)하기

### Q6. GitHub 원격 저장소를 연결한 직후, 다음 단계는 `git push -u origin main`인가요, 아니면 `git add .`인가요?
**A.** **로컬에서 커밋을 이미 마쳤다면 바로 `git push -u origin main`을 실행하면 됩니다.**  
* 작업 흐름의 기본 원칙:
  1. 파일 수정/추가
  2. `git add .` (스테이징)
  3. `git commit -m "메시지"` (로컬 저장)
  4. `git push -u origin main` (GitHub 원격 저장소로 업로드)
* 이미 커밋이 완료된 상태라면 `add`나 `commit`을 다시 할 필요 없이 바로 `push`를 진행합니다.

---

### Q7. GitHub 원격 저장소 연결 및 첫 푸시 명령어는 무엇인가요?
**A.**

```bash
# 1. GitHub 원격 저장소(origin) 등록
git remote add origin https://github.com/Paulkim3/chinese_text_preprocessing.git

# 2. 기본 브랜치 이름을 main으로 지정
git branch -M main

# 3. 원격 저장소로 푸시 (-u 옵션은 이후 git push만 입력해도 되도록 기본 업스트림 설정)
git push -u origin main
```

---

## 3. GitHub 설정 Private을 Public으로 전환하기 (주의사항 및 `.gitignore` 수정)

### Q8. 저장소를 Public으로 전환하기 전, 어떤 보안 사항을 반드시 점검해야 하나요?
**A.** 전 세계 누구나 코드를 열람할 수 있으므로 아래 4가지를 반드시 점검해야 합니다:
1. **API 키 및 비밀번호**: OpenAI API 키, 데이터베이스 접속 비밀번호 등이 코드에 하드코딩되어 있지 않은지 확인.
2. **개인 연락처/이메일**: 설정 파일에 개인 이메일이나 실명이 불필요하게 노출되지 않았는지 확인.
3. **가상환경(`.venv`) 및 임시 파일**: 가상환경 전체 파일이나 Mac 시스템 임시 파일(`.DS_Store`)이 올라가지 않도록 차단.
4. **깨진 링크(Broken Symlinks)**: 가상환경 패키지 내부를 가리키는 로컬 전용 심볼릭 링크(예: `.agents/`, `.claude/`)가 깃에 포함되지 않았는지 점검.

---

### Q9. 개인 이메일을 공개하고 싶지 않을 때 `pyproject.toml`을 어떻게 수정해야 하나요? `{ name = " ", email = " " }`처럼 빈칸으로 남겨도 되나요?
**A.** **빈칸이나 공백 문자열(`" "`)로 남겨두는 것은 권장하지 않습니다.**  
* 파이썬 패키지 빌드 도구나 `uv`에서 이메일 형식(`@` 포함 여부 등)을 검증할 때 문법 유효성 오류(Validation Error)를 일으킬 수 있습니다.
* **가장 좋은 방법**: `email` 속성만 지우고 이름/닉네임만 남겨두거나, `authors` 블록을 통째로 삭제합니다. (선택 사항 필드이므로 빌드/실행에 아무 영향이 없습니다.)

```toml
# 추천 형태: 이름만 남기기
authors = [
    { name = "Paulkim3" }
]
```

---

### Q10. 이미 깃에 올라간 불필요한 링크 폴더(`.agents`, `.claude`)는 로컬 파일을 유지하면서 깃에서만 어떻게 삭제하나요?
**A.** **`git rm -r --cached` 명령어를 사용합니다.**
* `--cached` 옵션을 붙이면 하드디스크의 실제 파일/폴더는 그대로 보존되고, **Git 추적 상태(인덱스)에서만 안전하게 제거**됩니다.

```bash
git rm -r --cached .agents .claude
```

---

### Q11. 보안과 청결성을 보장하는 최종 권장 `.gitignore` 내용은 무엇인가요?
**A.** 프로젝트 루트의 `.gitignore` 파일에 아래 내용을 적용합니다:

```gitignore
# Python-generated files (파이썬 컴파일 및 빌드 파일)
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info
*.log

# Virtual environments (가상환경 폴더 제외)
.venv/
env/
venv/

# Environment variables & secrets (API 키 및 비밀 환경변수 보호)
.env
.env.*

# macOS system files (맥 시스템 임시 메타데이터 제외)
.DS_Store
.AppleDouble
.LSOverride
._*

# IDE & Editors (에디터 설정 제외)
.vscode/
.idea/

# AI agent symlinks (로컬 가상환경 전용 심볼릭 링크 제외)
.agents/
.claude/
```

---

### Q12. GitHub 웹사이트에서 Private 저장소를 Public으로 전환하는 방법은?
**A.**
1. 브라우저에서 저장소 설정으로 이동:  
   `https://github.com/Paulkim3/chinese_text_preprocessing/settings`
2. 페이지 맨 아래 **Danger Zone**(위험 구역)으로 스크롤합니다.
3. **Change repository visibility** 항목의 **Change visibility** 버튼을 누릅니다.
4. **Make public**을 선택하고 저장소 이름을 입력하여 변경을 승인합니다.

---

## 4. GitHub 탑재물을 Streamlit Community에 올려 배포하기

### Q13. Streamlit Community Cloud에 앱을 배포하는 단계는 어떻게 되나요?
**A.**
1. **배포용 의존성 파일(`requirements.txt`) 생성 및 푸시**:
   ```txt
   streamlit>=1.40.0
   pandas
   numpy
   matplotlib
   ```
   * 위 파일을 루트에 생성하고 GitHub에 커밋 & 푸시합니다.
2. **Streamlit Cloud 접속 및 앱 생성**:
   * [share.streamlit.io](https://share.streamlit.io/)에 접속하여 GitHub 계정으로 로그인.
   * **New app** 버튼 클릭.
   * 배포 정보 입력:
     * **Repository**: `Paulkim3/chinese_text_preprocessing`
     * **Branch**: `main`
     * **Main file path**: `src/textpreprocessing/python_for_chinese.py`
     * **App URL**: 원하는 도메인명(예: `chinese-text-preprocessing`) 입력.
   * **Deploy!** 버튼 클릭.

---

### Q14. GitHub를 Public으로 변경했는데도 Streamlit 앱 접속 시 여전히 로그인을 요구하는 원인은 무엇인가요?
**A.** **Streamlit Cloud가 최초 배포 당시의 'Private' 접근 권한 설정과 캐시를 유지하고 있기 때문입니다.**
* GitHub 저장소를 나중에 Public으로 바꾸더라도, Streamlit 앱 설정 내부의 공유 범위(Sharing)가 자동으로 Public으로 전환되지 않거나 이전 인증 세션이 남아있어 발생합니다.

---

### Q15. 로그인 요구 문제를 해결하는 가장 확실한 방법은 무엇이며, 앱 리부트(Reboot)를 해도 되나요?
**A.**
1. **앱 리부트(Reboot app) 여부**:  
   * **네, 안심하고 진행하셔도 됩니다.**
   * 소스 코드와 설정은 모두 GitHub에 보존되어 있으므로 코드 손실 위험이 전혀 없습니다.
   * 대시보드의 점 세 개(`...`) 메뉴에서 `Reboot app`을 실행하면 서버 컨테이너가 갱신됩니다.
2. **가장 확실하고 빠른 해결책 (Delete 후 Redeploy, 1분 소요)**:  
   * 리부트 후에도 권한 캐시 때문에 로그인을 요구한다면, Streamlit 대시보드에서 해당 앱을 **Delete app(삭제)** 합니다.
   * 우측 상단 **New app**을 눌러 동일한 저장소 정보와 Custom URL을 입력하고 **Deploy**합니다.
   * 이미 GitHub가 Public인 상태에서 생성되므로, **로그인 없이 전 세계 누구나 즉시 접속 가능한 완전 공개 앱**으로 즉시 배포됩니다.

---

대화 ID: `agy --f0204422-ac49-4eef-9516-a9e271b050ed`
