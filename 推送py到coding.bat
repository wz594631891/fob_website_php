@echo off
@REM coding推送py脚本0422
echo 福步推送脚本:add commit push
git add .
set /p m=Commit
git commit -m "%m%"
git push origin master
pause