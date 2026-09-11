@echo off
chcp 65001 >nul
setlocal
title 27 pyeon fix

set "URL=https://github.com/buffysmg5-eng/ai/raw/claude/naver-market-blog-setup-11epes/market-blog/pkg47/content.json"
set "NEW=%TEMP%\mb27-content.json"

echo.
echo  ===========================================================
echo   27편 수정본 적용  -  엔 최저일 7/28 - 7/29 정정, 용어 병기
echo  ===========================================================
echo.
echo  [1/3] 수정본 내려받는 중...

if exist "%NEW%" del /q "%NEW%"
curl -sSL -o "%NEW%" "%URL%"
if not exist "%NEW%" goto FAIL
call :SIZE "%NEW%"
if %FSIZE% LSS 20000 goto FAIL
echo        받음 - %FSIZE% bytes
echo.
echo  [2/3] 27편 패키지 찾는 중...
echo.

rem  매칭은 27편에만 있는 ASCII 식별자 두 개로 한다 (한글 코드페이지 회피)
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
 "$new='%NEW%'; $hit=0;" ^
 "foreach($r in @('%~dp0','%~dp0..','%~dp0..\..')){" ^
 " Get-ChildItem -LiteralPath $r -Recurse -Filter content.json -ErrorAction SilentlyContinue | ForEach-Object {" ^
 "  $p=$_.FullName; if($p -ieq $new){return};" ^
 "  try{ $c=Get-Content -LiteralPath $p -Raw -Encoding UTF8 }catch{ return };" ^
 "  if(($c -like '*01-three-tiers.png*') -and ($c -like '*07-boj-taper.png*')){" ^
 "    $bak=$p+'.bak-'+(Get-Date -Format 'yyyyMMdd-HHmmss');" ^
 "    Copy-Item -LiteralPath $p -Destination $bak -Force;" ^
 "    Copy-Item -LiteralPath $new -Destination $p -Force;" ^
 "    $script:hit++; Write-Host ('   OK  ' + $p); Write-Host ('   bak ' + $bak); Write-Host '' } } };" ^
 "if($hit -eq 0){ exit 1 }"

if errorlevel 1 goto NOTFOUND

echo  [3/3] 교체 끝.
echo.

set "RUNBAT="
for %%F in ("%~dp0run-0911.bat" "%~dp0..\run-0911.bat" "%~dp0..\..\run-0911.bat") do (
  if exist "%%~F" if not defined RUNBAT set "RUNBAT=%%~F"
)

if not defined RUNBAT (
  echo  run-0911.bat 을 직접 실행하면 임시저장까지 갑니다.
  echo  images 폴더는 바뀐 것이 없으니 그대로 두세요.
  echo.
  pause
  exit /b 0
)

echo  run-0911.bat 을 찾았습니다:
echo    %RUNBAT%
echo.
echo  지금 이어서 실행할까요?
echo  (크롬 테스트 모드가 켜져 있고 네이버에 로그인돼 있어야 합니다)
echo.
choice /c YN /n /m "  실행 Y / 나중에 N : "
if errorlevel 2 goto SKIP

echo.
call "%RUNBAT%"
echo.
echo  퍼블리셔가 끝났습니다. 임시저장본을 눈으로 확인하세요.
echo    - 7절에 "7월 29일" 로 들어갔는지
echo    - 본문 글자 크기가 튀지 않는지 (19px 서식 누수)
echo    - 이미지 8장 순서와 캡션
echo.
pause
exit /b 0

:SKIP
echo.
echo  나중에 run-0911.bat 을 실행하면 됩니다.
echo.
pause
exit /b 0

:SIZE
set "FSIZE=%~z1"
exit /b

:FAIL
echo.
echo   [실패] 내려받기 실패. 인터넷 연결을 확인하거나
echo   아래 주소를 브라우저에서 직접 열어 저장하세요.
echo   %URL%
echo.
pause
exit /b 1

:NOTFOUND
echo.
echo   [찾지 못함] 27편 패키지를 찾지 못했습니다.
echo   이 파일을 프로젝트 폴더(큐가 들어 있는 폴더) 안에 두고
echo   다시 더블클릭해 주세요.
echo.
pause
exit /b 1
