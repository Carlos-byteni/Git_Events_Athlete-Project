## Git_Events_Athlete-Project
BackEnd Project about Events and Athlete interactions.
Este é um projeto de BackEnd que tem por objetivo a criação de uma
API rest para servir os dados do arquivo eventos históricos juegos olímpicos.
Nome do arquivo: "athlete_events.csv".

+ Nome do desenvolvedor: Carlos Ernesto Morales Alvarado.
+ email: alvarado.cem@gmail.com

### Tecnologías usadas

* Python
* Django
* sqlite3

### Descrição do projeto
Para o início do projeto foi criada uma pasta como o nome API_PROJECT. Dentro de esta
pasta estão o projeto específico chamado APIREST e a pasta do ambiente virtual (venv) que fue 
utilziado para esse projeto "atletas".

### Criação da aplicação
O nome da aplicação é olimpic. Dentro dessa aplicação foram trabalhados os seguintes 
arquivos.

### Modelos
*models.py: 
foram craidos os modelos do projeto. Dois prinicipais modelos
foram definidos
  *Modelo Personal: campos: Nome, Sex, Height, Weight, Team, NOC. 
  *Modelo Evento: campos: Games, Age, Year, Season, City, Sport, Event, Medal
  e personal que é a variável do relacionamento ManytoMany entre os dois modelos.
 
### Admin
 *admin.py
 Foram definidos registrados os modelos Personal e Evento no site admin do Django.
 
 *serializers.py
 Neste arquivo foram criados os serializadores de conversão de formatos de dados.
 São dois serializadores baseados na classe ModelSerializer, um para cada modelo do projeto.
 1. PersonalSerializer
 2. EventoSerializer
 
### Visualizações
 
 * views.py
 
 As visulizações contêm a lógica do projeto.
 Criação da classe do tipo ViewSet:
 
 + PersonalViewSet_ViewSet:
  Contém a lista do queryset do método GET e da recuperação dos objetos do modelo Personal no banco de dados
 + PersonalViewSet_ModelviweSet:
 Permite obter as ações: create, patch, put, destroy dos objetos.
 
 + EventoViewSet:
 Contém a lista do querey e dos métodos GET e da recuperação dos objetos do modelo Evento.
 +EventoViewSet_ModelviweSet:
 São permitidas as ações create, patch, put, destroy.
 
 Sempre neste em views.py, foi importado o arquivo "athlete_events.csv" e criada um rotina que insire os 
 registros desse arquivo no banco de dados do projeto.
 
 ### Urls da aplicação
 Arquivo olimpic.urls.py foi criado para fazer o mapeamento da rotas de acceso urls das visualizações do
 projeto. As urls da aplicação mostram os registros nos campos dos modelos, essas urls foram implementadas
 a partir de routers que vinculam a ulr com a informação das tabelas.
 
 ### Urls do Projeto
 Elas contêm o rota do site admin e da url vinculada a população do banco de dados do projeto.
 Essa urls está associada à urls da aplicação.
 
 ### Settings
 
 Em relação as configurações foram configurados os Installed_Apps ao inserir 'rest_framework' e a aplicação
 'olimpic'.
 
 
 
 
 










