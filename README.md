# Practices K8s

* Create a deployment with [game.yaml](k8s_manifests/game.yaml)
* Delete a pod from the deployment, observe the pods again
* Scale the deployment to 20 pods
* Scale down the deployment to 5 pods
* Stop the deployment from creating more pods without delete the deployment
* Exec into the pods
* Expose the deployment
* Follow this tutorials https://kubernetes.io/docs/concepts/services-networking/ingress/
  * Goal is to be able to access 2048 game from the internet over a public IP

* Check all K8s nodes health and status
* Check all K8s nodes' labels
* Let pods game-2048 only run on node test-cluster-7cz7fulwzgkx-node-0
