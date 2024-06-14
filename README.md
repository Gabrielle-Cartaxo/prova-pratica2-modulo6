# Segunda prova do módulo 6

Desenvolvimento da parte prática, com a detecção de faces de um vídeo utilizando Haar Cascade, e resposta a algumas perguntas técnicas.

## Perguntas técnicas

### 2.1.

**Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.**

O haar cascade é um modelo utilizado para a detecção de objetos, treinado com várias imagens positivas (com os objetos procurados) e negativas (sem os objetos). Nesse caso, o haar que está sendo utilizado nesse projeto foi treinado com diferentes rostos. Para inferir se uma imagem possui rostos ou não, ele analisa a imagem passando os pixels por "quadradinhos", que por meio de uma convolução devolvem certas características, identificando assim as faces.

![Quadradinhos do Haar Cascade](/static/image.png)



### 2.2

**Considere as seguintes alternativas para resolver o problema de detecção de faces:**

- HAAR Cascade
- CNN
- NN Linear
- Filtros de correlação cruzada

**Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.**

Irei avaliar do mais simples até o mais complexo:

- NN Linear: Linear Neural Network. Não é tão útil em processamento de imagens porque por ser linear, não consegue identificar padrões e correlações entre as entradas, dificultando a detecção de objetos.

- Haar Cascade: É um modelo bem leve e que já está disponivel com o treinamento na internet. Seu processamento também é bem rápido, e é capaz de detectar objetos em situações simples. Funciona melhor em imagens preto e branco e detecta apenas aquilo para o que foi treinado. Por isso, mesmo que só pra detecção de faces, há diferentes Haar Cascades para download, com diferentes posições: frontal, na diagonal, de lado etc. Logo, é útil para aplicações simplistas (como essa prova), mas não é muito versátil.

- Filtros de Correlação Cruzada: Coloquei ele em terceiro lugar em relação ao Haar Cascade porque para usar esse aqui, é necessário criar um dataset para uma aplicação bem específica. Porém, em questão de versatilidade, eu diria que é o menos versátil das opções mencionadas. Para explicar como ele funciona, irei usar o exemplo da aula: se eu quero detectar apenas o rosto do Ronaldinho Gaúcho, eu posso criar um filtro que consiste numa foto do mesmo, e comparar com as imagens de entrada para verificar se há as características dele. Por ser um filtro específico (como o rosto do Ronaldinho), dificilmente é possível usar esse filtro para aplicações diversas.

- CNN: Convolucional Neural Network. É o melhor tipo de modelo a se utilizar na detecção de objetos em imagens, pois através da convolução em várias camadas, ele é capaz de identificar padrões e correlacionar as informações (coisas que o modelo linear não consegue), sendo a aplicação mais versátil de todas. Porém, requer um grande treinamento para que funcione da melhor maneira, além de costumar ser bem mais pesado do que os outros modelos mencionados. Um exemplo de CNN é o YOLO, que apesar de ter um desempenho muito bom (detectar objetos e rostos com facilidade quando treinado), ocupa bastante espaço.
Logo, é um trade-off a se considerar, tendo mais aplicabilidade em situações mais complexas.


### 2.3.

**Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.**

- NNL: Não consegue realizar a tarefa ou se consegue, imagino que a acurácia seria muito baixa, porque esse tipo de modelo não observa padrões (causalidade) na hora de avaliar a imagem. Logo, dificilmente teria essa avaliação do rosto como um todo.

- Filtro de Correlação Cruzada: Acredito que seria possível usar esse em casos que só queremos detectar um tipo de emoção, usando como filtro a foto de alguém sorrindo, por exemplo. Mas, para a detecção de emoções diversas, acho que ele não conseguiria classificar.

- Haar Cascade: De maneira semelhante ao FCC que foi citado acima, imagino que dê para fazer a classificação apenas de uma emoção por vez, usando um filtro para os olhos, outro para a boca e juntando as informações, determinar se aquela expressão é feliz. Porém, também não acredito que tenha exatamente uma versatilidade nessa aplicação.

- CNN: Acredito que por se tratar de uma aplicação um pouco mais complexa, como avaliar não apenas rostos, mas padrões nos mesmos, o CNN seria a melhor opção, pois pode ser treinado com informações diversas, ou seja, com diferentes emoções, sendo possível criar padrões. 

### 2.4.

**A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?**

Eu diria que apenas as redes neurais fazem isso, já que ajustar os pesos conforme o erro a fim de melhorar a predição é a base de como funicionam os perceptrons, que compõem essas redes, tal qual LNN e CNN. Porém, para o contexto de imagens, diria que o modelo que melhor emprega isso é o CNN.


## Como executar a atividade da prova!

Para cumprir a atividade de receber um vídeo, detectar faces nele e devolver o vídeo com retângulos ao redor das faces, fiz um servidor usando Flask que mostra o resultado do vído pós detecção de imagem, usando dois modelos de Haar Cascade.

Para executar o projeto, primeiramente clone este repositório e vá para a pasra `src`. 

```bash
cd src

```

Depois, crie um ambiente virtual para instalar as dependências. (Caso não tenha o python instalado, primeiro faça isso, depois execute o comando abaixo.)

```bash
python3 -m venv venv

```

Depois, ative o ambiente virtual:

Para Windows:

```bash
cd venv\Scripts\activate
```
Para Linux:

```bash
source venv/bin/activate

```

Com o ambiente virtual ativado, instale as dependências:

```bash
pip install Flask
pip install opencv-python

```

Depois, vá para a pasta src e execute o seguinte comando:

```bash
python app.py

```

Assim, pode acessar seu navegador no endereço que aparecer no terminal, que costuma seguir a estrutura `http://{localhost}:8000`, substituindo o localhost pelo seu ip.
Só apertar cntrl e clicar no link que irá te redirecionar para o site.


Para visualizar um vídeo desse sistema funcionando, pode acessar [esse link!](https://www.youtube.com/watch?v=t1PB-BVdVLs)



