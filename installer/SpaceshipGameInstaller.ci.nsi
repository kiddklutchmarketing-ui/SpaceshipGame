!include "MUI2.nsh"

Name "Spaceship Game"
OutFile "releases\\SpaceshipGameInstaller.exe"
InstallDir "$PROGRAMFILES64\\Spaceship Game"

!insertmacro MUI_PAGE_LICENSE "README.md"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

Section "Install"
  SetOutPath "$INSTDIR"
  File "dist\\SpaceshipGame.exe"
  File /r "assets\\*.*"
  CreateShortCut "$DESKTOP\\Spaceship Game.lnk" "$INSTDIR\\SpaceshipGame.exe"
SectionEnd
