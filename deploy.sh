cd ../scrum-tools-front/
ng build
rm -rf ../scrum-tools-flask/en-US
mv dist/scrum-tools-front/en-US ../scrum-tools-flask/
cd ../scrum-tools-flask/
git add -A
git commit -a -m "deploy.sh"
git push