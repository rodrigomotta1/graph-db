# Teste prático do TigerGraph

# Setup
1. Baixar o Docker
2. Baixar o WSL
3. Inicialiazar o WSL
4. Dentro do WSL, criar uma pasta compartilhada com o container
```bash
mkdir shared_folder
chmod 777 shared_folder
```
5. Baixar a imagem do TigerGraph
```bash
docker pull docker.tigergraph.com/tigergraph-dev:latest
```
6. Rodar a imagem criando um container
```bash
docker run -d -p 14022:22 -p 9000:9000 -p 14240:14240 --name tigergraph_dev --ulimit nofile=1000000:1000000 -v ~/shared_data
```
7. Checar se o container está rodando
```bash
docker ps | grep tigergraph
```
8. Se estiver tudo ok, o container estará rodando em *background*. Para conectar-se ao container, rodar o comando abaixo, entrando a senha padrão `tigergraph`:
```bash
ssh -p 14022 tigergraph@localhost
```
9. Ao logar, os serviços disponíveis são:
   - `gadmin start`
   - `gsql`
   - o `GraphStudio` estará disponível na máquina local em `localhost:14240`

10.Para encerrar ou inicializar:
```bash
docker container stop tigergraph_dev
docker container start tigergraph_dev
```