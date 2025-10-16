
import google.generativeai as genai
import os

# Configure the Gemini API key
# Make sure to set the GOOGLE_API_KEY environment variable in your system.
# genai.configure(api_key=os.environ["GOOGLE_API_KEY"]) You can use this line if you have the key in your environment.
genai.configure(api_key="YOUR_API_KEY") # Replace with your key if you don't have it in your environment.


# The extracted and formatted FAQ data
faq_data = [
    {"question": "Porque é que o meu congelador congela demais?", "answer": "Se num curto período de tempo se formam grandes quantidades de gelo, deve verificar o seguinte: Certifique-se que a funç..."},
    {"question": "Quando utilizo a máquina de lavar roupa, qual é a quantidade de detergente ideal para cada carga?", "answer": "Depende da dureza da água e da sujidade da roupa. Uma água macia requer um pouco menos de detergente do que uma água dur..."},
    {"question": "Será que posso colocar um frigorífico de bancada no chão da minha cozinha?", "answer": "Sim, mas verifique que tem espaço suficiente para uma ventilação correta."},
    {"question": "Será melhor utilizar produtos 4 em 1 ou detergente, sal e abrilhantador em separado?", "answer": "Utilizar detergente, sal e abrilhantador em separado permite-lhe ajustar a mistura ao tipo de água da sua zona e à quant..."},
    {"question": "O congelador trabalha de forma adequada se estiver muito frio ou muito calor na divisão onde for colocado?", "answer": "Sim. Deverá apenas assegurar-se de que a temperatura definida é adequada. A temperatura não deve ser inferior a 4ºC ou s..."},
    {"question": "Posso utilizar a minha placa a gás em caso de corte de eletricidade?", "answer": "No caso de ocorrer um corte de eletricidade prolongado, os queimadores podem ser ligados manualmente. Acenda um fósforo ..."},
    {"question": "Quando é que o programa de pré-lavagem é necessário?", "answer": "Apenas quando a sua roupa está muito suja."},
    {"question": "Como proteger os alimentos durante uma interrupção da corrente elétrica?", "answer": "Caso ocorra uma falha elétrica, o tempo em que o congelador ficará frio varia. Um congelador cheio fica frio mais tempo ..."},
    {"question": "Qual o diâmetro do tubo de ventilação que devo usar para um exaustor ilha?", "answer": "Idealmente, deve usar um tubo de ventilação de 150 mm de diâmetro, mas está disponível um kit que o reduz para 120 mm, q..."},
    {"question": "Posso utilizar sal de mesa na minha máquina de lavar loiça?", "answer": "O sal de cozinha geralmente contém ingredientes que podem danificar a máquina de lavar loiça."},
    {"question": "Qual a distância mínima necessária entre a placa e o exaustor?", "answer": "Para uma placa a gás da Whirlpool com menos de 7500W de potência, a distância mínima é de 65cm. Para placas com potência..."},
    {"question": "Quanto espaço devo deixar à volta do frigorífico?", "answer": "Com congeladores de livre instalação deve deixar 5 cm na parte de cima e 10 cm entre a parte de trás do aparelho e a par..."},
    {"question": "Tenho de descongelar o congelador mais frequentemente do que o que indica o manual. Qual será a razão?", "answer": "A borracha do isolamento da porta pode estar gasta. Para comprovar, tente fechar a porta com um papel entre a borracha e..."},
    {"question": "Qual a temperatura ideal para instalar uma garrafeira?", "answer": "A garrafeira da Whirlpool irá funcionar na perfeição em locais com temperaturas entre os 6 e os 32 graus."},
    {"question": "É necessário utilizar um abrilhantador na minha máquina de lavar loiça?", "answer": "Recomendamos a utilização de um abrilhantador, pois é essencial para uma boa secagem. Assegure-se de que encheu o distri..."},
    {"question": "No dispensador, a luz vermelha referente ao filtro está acesa. Como deve estar a luz?", "answer": "A vida útil do filtro de água é de seis meses. O indicador muda de verde para laranja aos 90% do seu período de vida úti..."},
    {"question": "Quando é que tenho de juntar abrilhantador no dispensador?", "answer": "O indicador LED acende quando é necessário adicionar o abrilhantador. O abrilhantador favorece o processo de secagem e e..."},
    {"question": "Qual é a diferença entre um secador por condensação e um secador por ventilação?", "answer": "Os secadores por ventilação são fornecidos com um kit de ventilação que canaliza o ar para fora do aparelho. Os secadore..."},
    {"question": "Qual a distância mínima entre uma placa e um exaustor?", "answer": "Por favor, verifique o manual de instruções dos seus produtos em particular. Normalmente, aconselhamos distância de 750 ..."},
    {"question": "As portas dos frigoríficos e congeladores de bancada de 45,8 cm são reversíveis?", "answer": "Este tipo de aparelhos não tem portas reversíveis. Os conjuntos de uma porta (frigorífico e congelador) têm as portas po..."},
    {"question": "A água potável do dispensador tem um leve gosto químico. Como posso evitar?", "answer": "A água potável deve ser usada regularmente, para evitar que fique armazenada sem ser mudada durante longos períodos."},
    {"question": "Preparei um prato de peixe no microondas. Como posso remover o cheiro desagradável?", "answer": "Aqueça uma chávena de água contendo umas gotas de limão durante cerca de um minuto. Isto irá remover qualquer odor desag..."},
    {"question": "Que quantidade de detergente devo utilizar na minha máquina de lavar loiça?", "answer": "A quantidade de detergente a utilizar depende da dureza da água e do tipo de detergente. Se utilizar uma quantidade insu..."},
    {"question": "Qual a temperatura ideal para o meu frigorífico e para o meu congelador?", "answer": "É aconselhável uma temperatura média de 3 ou 4ºC, com um limite mais baixo de 0ºC e mais alto de 7ºC. A 7ºC, os alimento..."},
    {"question": "Porque é que alguns vendedores recomendam que se lave a roupa do avesso?", "answer": "Virar a roupa do avesso evita o desgaste, reduzindo a formação de borbotos e preservando os tecidos. Além disso, qualque..."},
    {"question": "São necessários filtros especiais para um exaustor de recirculação?", "answer": "Sim, necessita de um filtro especial para a gordura e os odores. Consiste normalmente num cartucho cheio de grãos de car..."},
    {"question": "O que significam as luzes do congelador?", "answer": "A luz VERDE indica que o aparelho está ligado à corrente. Em conjunto com o botão, a luz LARANJA indica que a função Con..."},
    {"question": "As placas de indução necessitam de um tipo específico de panelas?", "answer": "As panelas têm de ser em metal ferroso. Pode verificar se as suas panelas estão adequadas utilizando um íman de frigoríf..."},
    {"question": "As placas da Whirlpool podem ser usadas com gás Butano?", "answer": "Sim, existem kits de conversão para gás butano disponíveis para todas as placas da Whirlpool, podendo ser adquiridos atr..."},
    {"question": "Quanto tempo demora o aparelho a fazer gelo?", "answer": "A máquina de gelo não vai fazer gelo até a temperatura do congelador estar abaixo dos -12ºC e irá demorar um dia para en..."},
    {"question": "Não consigo instalar uma conduta externa para o meu exaustor. Será que a recirculação é uma boa ideia?", "answer": "Sim. Todos os exaustores da Whirlpool podem ser usados tanto em modo de extração como recirculação. A recirculação remov..."},
    {"question": "O que é que causa o borboto em algumas roupas?", "answer": "Muitas roupas sintéticas libertam fibras que provocam a formação de borboto. Sobrecarregar a máquina pode propiciar esta..."},
    {"question": "Existem vários níveis de consumo energético. Por qual devo optar?", "answer": "As classes de eficiência energética A e A+ oferecem os consumos energéticos mais reduzidos. Isto significa que esses ele..."},
    {"question": "Tenho uma placa de 68 cm. É necessário um exaustor de 90 cm para a minha placa?", "answer": "Não, desde que siga as instruções e coloque o exaustor e a placa à distância correta."},
    {"question": "Qual é o comprimento máximo da conduta de ventilação que posso ter no meu exaustor?", "answer": "Idealmente, não mais que 3 metros."},
    {"question": "Existe água na parte inferior do meu frigorífico de descongelação automática. Porquê?", "answer": "É provável que o tubo de drenagem utilizado para escoar e presente na parte traseira do frigorífico esteja bloqueado. Is..."},
    {"question": "Que produtos de limpeza devo evitar utilizar na limpeza do meu frigorífico?", "answer": "Não utilize detergentes abrasivos, tais como os produtos de limpeza para os vidros, esfregões, produtos de limpeza infla..."},
    {"question": "Os queimadores da placa estão manchados e sem cor. Como posso limpá-los?", "answer": "A melhor forma de os limpar é com um detergente próprio para limpar cromo (Solvol Autosol). Deve ter cuidado para não bl..."},
    {"question": "Posso colocar um secador na parte superior da máquina de lavar roupa?", "answer": "A máquina de lavar roupa deve ser colocada no chão, pois é a mais pesada. Na sua maioria, os equipamentos da mesma marca..."},
    {"question": "A temperatura no interior do equipamento está demasiado fria/quente. Quais as definições de temperatura corretas?", "answer": "A temperature ótima normal no centro dos compartimentos deve ser a seguinte: Frigorífico +3.5°C; Gaveta Crisper 0°C; Con..."},
    {"question": "Como devo limpar e cuidar das superfícies em aço inoxidável?", "answer": "Use um detergente líquido ou um produto de limpeza multiusos. Enxague com água limpa e seque com um pano macio, isento d..."},
    {"question": "Porque não posso usar objetos de metal no microondas?", "answer": "A radiação do microondas é refletida pelo metal. Uma radiação demasiado forte dirigida para um só ponto provocará queima..."},
    {"question": "Como posso eliminar os maus odores do meu frigorífico?", "answer": "Limpe o interior com um detergente de limpeza suave. Obtenha os melhores resultados utilizando os detergentes adequados."},
    {"question": "Qual é a melhor forma de limpar o meu frigorífico?", "answer": "Limpe os compartimentos do frigorífico e do congelador mais ou menos uma vez por mês para evitar a formação de odores. P..."},
    {"question": "O aro cromado em redor da placa de aquecimento está a ficar sem cor. É normal?", "answer": "O aro é feito de aço inoxidável para evitar a corrosão. Alterações na cor devido à alta temperatura da placa de aquecime..."},
    {"question": "Que produtos devo evitar utilizar na limpeza das superfícies de aço inoxidável?", "answer": "Evite os esfregões com sabão desengordurante, produtos de limpeza abrasivos, cremes de polir, esfregões de arame, panos ..."},
    {"question": "Que tipo de utensílios de cozinha posso utilizar no microondas?", "answer": "Consulte as recomendações do fabricante ao usar: papel de alumínio, metal, plástico, sacos de plástico, tampas, loiças, ..."},
    {"question": "Como devo limpar o vidro do meu forno?", "answer": "Utilize um produto de limpeza para vidros e um pano macio ou uma esponja. Não utilize produtos de limpeza abrasivos, esf..."},
    {"question": "Como posso registar o meu eletrodoméstico Whirlpool?", "answer": "Pode registar o(s) seu(s) eletrodoméstico(s) Whirlpool no nosso website através do seguinte link. Em alternativa pode c..."},
    {"question": "Que exaustores podem ser ventilados pela parte de trás?", "answer": "Apenas o exaustor decorativo pode ser ventilado a partir da retaguarda."},
    {"question": "Quais as vantagens de registar o seu eletrodoméstico Whirlpool?", "answer": "Pode registar o seu eletrodoméstico Whirlpool connosco, independentemente de ter sido comprado através de um dos nossos ..."},
]

def find_best_answer(user_question, faq_data):
    """
    Finds the best answer from the FAQ data based on the user's question.
    """
    
    # Create a list of the questions from the FAQ data
    faq_questions = [item["question"] for item in faq_data]
    
    # Create a model for embeddings
    model = 'models/embedding-001'
    
    # Create embeddings for the user's question and the FAQ questions
    user_embedding = genai.embed_content(model=model,
                                          content=user_question,
                                          task_type="RETRIEVAL_QUERY")
    
    faq_embeddings = genai.embed_content(model=model,
                                         content=faq_questions,
                                         task_type="RETRIEVAL_DOCUMENT")
    
    # Find the best match using dot product
    best_match_index = -1
    highest_similarity = -1
    
    for i, faq_embedding in enumerate(faq_embeddings['embedding']):
        similarity = sum([a * b for a, b in zip(user_embedding['embedding'], faq_embedding)])
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match_index = i
            
    # Return the best answer
    return faq_data[best_match_index]["answer"]


def main():
    """
    The main function of the chatbot.
    """
    print("Olá! Eu sou o chatbot de FAQ da Whirlpool. Como posso ajudar?")
    
    while True:
        user_question = input("> ")
        if user_question.lower() in ["sair", "exit"]:
            break
        
        answer = find_best_answer(user_question, faq_data)
        print(answer)

if __name__ == "__main__":
    main()
