#  cd Devops-material-linkedin/devops-setup/
# . /home/sdutta/.nix-profile/etc/profile.d/nix.sh
##  export NIXPKGS_ALLOW_UNFREE=1
## nix-shell --run $SHELL
## kind create cluster --name my-3-node-cluster --config kind-cluster.yaml
## kind delete cluster --name my-3-node-cluster
## kubectl cluster-info --context kind-my-3-node-cluster
kubectl get pods nginx-pod -n base-namespace -o yaml
kubectl exec -it -n base-namespace nginx-pod -- /bin/bash

--docker---
docker rm -f $(docker ps -aq) 2>/dev/null || true
docker rmi -f $(docker images -aq) 2>/dev/null || true
docker system prune -a -f --volumes