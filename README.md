# LearnSail

Lo primero que tenemos que hacer es generar la imagen, en este caso la generaremos de manera de desarrollo la de release no la pude generar por mi equipo:

```
git submodule add https://github.com/lakehq/sail .submodules/sail
```

Cualquier persona que clone tu repo deberá hacer:

```
git submodule update --init --recursive
```

O clomnamos con

```
git clone --recurse-submodules <repo-url>
```

## k8s

```
kind create cluster
```

Generamos la imagen docker, pero para que funcione de momento hay que cambiar

```
Linux
sed -i 's/args: \[ "spark", "server", "--port", "50051" \]/args: ["spark", "server", "--ip", "0.0.0.0", "--port", "50051"]/' .submodules/sail/k8s/sail.yaml
MAC
sed -i '' 's/args: \[ "spark", "server", "--port", "50051" \]/args: ["spark", "server", "--ip", "0.0.0.0", "--port", "50051"]/' .submodules/sail/k8s/sail.yaml
```

```
docker build -t sail:latest -f ".submodules/sail/docker/release/Dockerfile" --build-arg RELEASE_TAG="main" --build-arg RUST_PROFILE="dev" . && \
kind load docker-image sail:latest && \
kubectl apply -f .submodules/sail/k8s/sail.yaml
```

Generamos un cliente básico

```
docker build -t pyspark-client:latest -f "./basic_example/Dockerfile" . && \
kind load docker-image pyspark-client:latest && \
kubectl apply -f "./basic_example/job.yaml"
```
