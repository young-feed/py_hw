pipeline {
    agent any

    stages {
        stage('Information') {
            steps {
                // Вывод сообщения с выбранным параметром ENV
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Deploy via SSH') {
            steps {
                // Плагин Publish Over SSH для копирования файлов
                sshPublisher(publishers: [
                    sshPublisherDesc(
                        configName: 'remote-server',
                        transfers: [
                            sshTransfer(
                                sourceFiles: '**/*', 
                                removePrefix: '', 
                                remoteDirectory: "/deploy_${params.ENV}" // Файлы попадут в /tmp/deploy_dev или /tmp/deploy_prod
                            )
                        ],
                        usePromotionTimestamp: false,
                        useWorkspaceInPromotion: false,
                        verbose: true
                    )
                ])
            }
        }
    }

    post {
        always {
            // Очистка рабочей директории в конце сборки
            cleanWs()
            echo "Workspace has been cleaned."
        }
    }
}
