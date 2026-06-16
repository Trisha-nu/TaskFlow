pipeline {
 agent any
 stages {
  stage('Install'){steps{sh 'pip install -r requirements.txt'}}
  stage('Verify'){steps{sh 'python -m py_compile app.py'}}
  stage('Docker'){steps{sh 'docker build -t taskflow .'}}
 }
}