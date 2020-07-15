pipeline {
    agent any
    stages {
        stage('Pull') {
            steps {
                sh "git pull || git clone git@gitlab:morbargig/test.git ."
            }
            stage("Build"){
                sh "docker build -t cowsay ."
            }
            stage("Test"){
                sh "docker run -d --name cowtest --net cowsay_default cowsay"
                script {
                    3.times {
                        try {
                            RESPONSE = sh ( script: "/bash/sh -c'wget --spider -S http://cowtest:8090 2>&1 | grep HTTP/'", returnStdout: true ).trim()
                        } catch (all) {
                            sh 'conection fial'
                            sh "sleep 5"
                        }
                    }
                    if ( "$RESPONSE" == "HTTP/1.1 200 OK" ){  
                        sh "echo conection success"
                    } else {
                        currentBuild.result = 'ABORTED'
                        error('Test failed, stopping…')
                    }        

                }
            }
            // stage("Publish"){
            //     script{
            //         docker.withRegistry("https://your.ecr.domain.amazonws.com", "ecr:us-east-1:credential-id") {
            //         docker.image("your-image-name").push()
            //     }
            // }
        }
    } 
}
