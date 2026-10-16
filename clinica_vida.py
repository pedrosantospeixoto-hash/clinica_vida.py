<!DOCTYPE html>
<html lang="pt-BR" class="h-full bg-slate-900">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Clínica Vida+ | Sistema Integrado Acadêmico</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');
    body { font-family: 'Inter', sans-serif; }
    code, pre { font-family: 'Fira Code', monospace; }
    .tab-btn.active {
      background-color: #0284c7;
      color: white;
      border-color: #0284c7;
    }
    @media print {
      .no-print { display: none !important; }
      .print-only { display: block !important; }
      body { background-color: white !important; color: black !important; }
      .print-card { border: 1px solid #ccc !important; box-shadow: none !important; }
    }
  </style>
</head>
<body class="h-full text-slate-100 flex flex-col antialiased selection:bg-sky-500 selection:text-white">

  <!-- Header Top Bar -->
  <header class="bg-slate-950/80 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50 no-print">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-emerald-400 flex items-center justify-center shadow-lg shadow-sky-500/20">
            <i class="fa-solid font-bold fa-heart-pulse text-white text-xl"></i>
          </div>
          <div>
            <h1 class="font-bold text-lg text-white tracking-wide leading-none">CLÍNICA VIDA<span class="text-sky-400">+</span></h1>
            <span class="text-xs text-slate-400 font-medium">Plataforma Acadêmica de Gestão</span>
          </div>
        </div>
        
        <!-- Global Actions -->
        <div class="flex items-center space-x-2 sm:space-x-3">
          <button onclick="baixarCodigoPython()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600/20 text-emerald-400 border border-emerald-500/30 hover:bg-emerald-600/30 transition flex items-center space-x-2">
            <i class="fa-solid fa-download"></i>
            <span class="hidden md:inline">Baixar Python (.py)</span>
          </button>
          <button onclick="exportarRelatorioCompleto()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-600/20 text-sky-400 border border-sky-500/30 hover:bg-sky-600/30 transition flex items-center space-x-2">
            <i class="fa-solid fa-file-export"></i>
            <span class="hidden md:inline">Exportar Relatório</span>
          </button>
          <button onclick="window.print()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-200 border border-slate-700 hover:bg-slate-700 transition flex items-center space-x-2">
            <i class="fa-solid fa-print"></i>
            <span class="hidden sm:inline">Imprimir</span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <nav class="bg-slate-900 border-b border-slate-800 no-print">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex space-x-1 sm:space-x-2 overflow-x-auto py-2 scrollbar-none">
        <button onclick="setTab('passo0')" id="tab-passo0" class="tab-btn active px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-house"></i>
          <span>Visão Geral & Capa</span>
        </button>
        <button onclick="setTab('passo1')" id="tab-passo1" class="tab-btn px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent text-slate-400 hover:text-white transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-kanban"></i>
          <span>1. Trello Ágil</span>
        </button>
        <button onclick="setTab('passo2')" id="tab-passo2" class="tab-btn px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent text-slate-400 hover:text-white transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-code"></i>
          <span>2. Script Python</span>
        </button>
        <button onclick="setTab('passo3')" id="tab-passo3" class="tab-btn px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent text-slate-400 hover:text-white transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-microchip"></i>
          <span>3. Lógica Booleana</span>
        </button>
        <button onclick="setTab('passo4')" id="tab-passo4" class="tab-btn px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent text-slate-400 hover:text-white transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-layer-group"></i>
          <span>4. Fila FIFO</span>
        </button>
        <button onclick="setTab('passo5')" id="tab-passo5" class="tab-btn px-3.5 py-2 rounded-lg text-xs font-medium border border-transparent text-slate-400 hover:text-white transition flex items-center space-x-2 whitespace-nowrap">
          <i class="fa-solid fa-diagram-project"></i>
          <span>5. Casos de Uso UML</span>
        </button>
      </div>
    </div>
  </nav>

  <!-- Main Content Container -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

    <!-- SEÇÃO 0: Visão Geral / Capa / Introdução -->
    <section id="sec-passo0" class="tab-content space-y-6">
      <div class="bg-gradient-to-br from-slate-950 via-slate-900 to-sky-950 border border-slate-800 rounded-2xl p-6 sm:p-10 shadow-2xl relative overflow-hidden">
        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-sky-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="max-w-3xl space-y-4">
          <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-sky-500/10 text-sky-400 border border-sky-500/20">
            Projeto Integrador Acadêmico 2026
          </span>
          <h2 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight">
            Sistema Unificado de Gestão de Atendimentos <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-emerald-400">Clínica Vida+</span>
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Plataforma acadêmica completa integrando metodologia ágil, simulação de lógica operacional em Python, álgebra booleana aplicada à triagem médica, controle de estruturas de dados FIFO e diagrama estrutural UML de casos de uso.
          </p>
          <div class="pt-4 grid grid-cols-2 sm:grid-cols-4 gap-4 border-t border-slate-800/80 text-xs text-slate-400">
            <div><span class="block text-slate-500 font-medium">Instituição:</span> Faculdade de Tecnologia</div>
            <div><span class="block text-slate-500 font-medium">Curso:</span> Eng. de Software</div>
            <div><span class="block text-slate-500 font-medium">Autor:</span> Equipe Acadêmica</div>
            <div><span class="block text-slate-500 font-medium">Status:</span> 100% Funcional</div>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-3">
          <h3 class="text-lg font-bold text-white flex items-center space-x-2">
            <i class="fa-solid fa-circle-info text-sky-400"></i>
            <span>Introdução do Projeto</span>
          </h3>
          <p class="text-slate-300 text-sm leading-relaxed">
            A <strong>Clínica Vida+</strong> demanda alta precisão na gestão de seus atendimentos. O presente projeto visa eliminar gargalos operacionais através da formalização de 5 passos estratégicos: planejamento Kanban, automação de dados em Python, formalização lógica matemática das regras de liberação de consulta, enfileiramento sequencial sem desvio e especificação formal de papéis (médico e secretária).
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-3">
          <h3 class="text-lg font-bold text-white flex items-center space-x-2">
            <i class="fa-solid fa-bullseye text-emerald-400"></i>
            <span>Objetivos do Sistema</span>
          </h3>
          <ul class="text-slate-300 text-sm space-y-2 list-disc list-inside">
            <li>Garantir visibilidade ágil da evolução do desenvolvimento via Trello.</li>
            <li>Fornecer estatísticas populacionais de pacientes com verificação de erro.</li>
            <li>Eliminar ambiguidades na liberação de consultas normais e emergenciais.</li>
            <li>Assegurar a ordem cronológica estrita de atendimento via Fila FIFO.</li>
            <li>Definir limites de segurança de dados através da especificação UML.</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 1: Quadro Kanban estilo Trello -->
    <section id="sec-passo1" class="tab-content hidden space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-slate-950 p-4 border border-slate-800 rounded-2xl">
        <div>
          <h3 class="text-lg font-bold text-white">Passo 1: Quadro Visual de Gestão Ágil</h3>
          <p class="text-xs text-slate-400">Sprints, acompanhamento de tarefas, métricas e relatórios da Clínica Vida+</p>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="mostrarRelatorioSprint()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 text-white hover:bg-sky-500 transition flex items-center space-x-1.5">
            <i class="fa-solid fa-chart-line"></i>
            <span>Ver Relatório de Sprint</span>
          </button>
          <button onclick="mostrarGuiaTrelloReal()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition flex items-center space-x-1.5">
            <i class="fa-brands fa-trello text-sky-400"></i>
            <span>Como Criar no Trello</span>
          </button>
        </div>
      </div>

      <!-- Kanban Board Grid -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <!-- Backlog -->
        <div class="bg-slate-950/60 border border-slate-800 rounded-xl p-3 flex flex-col h-[500px]">
          <div class="flex items-center justify-between mb-3 px-1">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-slate-500"></span> Backlog
            </span>
            <span class="text-xs px-2 py-0.5 bg-slate-800 rounded-full text-slate-400 font-mono" id="count-backlog">2</span>
          </div>
          <div class="flex-1 space-y-2 overflow-y-auto pr-1" id="list-backlog">
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Sprint 3</span>
              <h4 class="text-xs font-semibold text-white">Integração com API de Telemedicina</h4>
              <p class="text-[11px] text-slate-400">Permitir chamadas de vídeo seguras diretamente da plataforma.</p>
              <div class="flex justify-between items-center text-[10px] text-slate-500 pt-2 border-t border-slate-800">
                <span>Prazo: 28/10</span>
                <button onclick="moverTarefa(this, 'sprint')" class="hover:text-sky-400">Avançar &rarr;</button>
              </div>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Sprint 3</span>
              <h4 class="text-xs font-semibold text-white">Notificações por SMS/WhatsApp</h4>
              <p class="text-[11px] text-slate-400">Lembrete automático 24h antes da consulta.</p>
              <div class="flex justify-between items-center text-[10px] text-slate-500 pt-2 border-t border-slate-800">
                <span>Prazo: 30/10</span>
                <button onclick="moverTarefa(this, 'sprint')" class="hover:text-sky-400">Avançar &rarr;</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Sprint Atual -->
        <div class="bg-slate-950/60 border border-slate-800 rounded-xl p-3 flex flex-col h-[500px]">
          <div class="flex items-center justify-between mb-3 px-1">
            <span class="text-xs font-bold text-sky-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-sky-400"></span> Sprint Atual
            </span>
            <span class="text-xs px-2 py-0.5 bg-sky-950 text-sky-400 rounded-full font-mono" id="count-sprint">2</span>
          </div>
          <div class="flex-1 space-y-2 overflow-y-auto pr-1" id="list-sprint">
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20">Sprint 2</span>
              <h4 class="text-xs font-semibold text-white">Validação Lógica das Consultas</h4>
              <p class="text-[11px] text-slate-400">Construção das tabelas-verdade de 16 combinações.</p>
              <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                <div class="bg-sky-400 h-full w-3/4"></div>
              </div>
              <div class="flex justify-between items-center text-[10px] text-slate-500 pt-1">
                <span>Checklist: 3/4</span>
                <button onclick="moverTarefa(this, 'progresso')" class="hover:text-sky-400">Avançar &rarr;</button>
              </div>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-sky-500/10 text-sky-400 border border-sky-500/20">Sprint 2</span>
              <h4 class="text-xs font-semibold text-white">Módulo Python de Cadastro</h4>
              <p class="text-[11px] text-slate-400">Lógica em loop com tratamentos de exceção.</p>
              <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                <div class="bg-sky-400 h-full w-1/2"></div>
              </div>
              <div class="flex justify-between items-center text-[10px] text-slate-500 pt-1">
                <span>Checklist: 2/4</span>
                <button onclick="moverTarefa(this, 'progresso')" class="hover:text-sky-400">Avançar &rarr;</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Em Progresso -->
        <div class="bg-slate-950/60 border border-slate-800 rounded-xl p-3 flex flex-col h-[500px]">
          <div class="flex items-center justify-between mb-3 px-1">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-amber-400"></span> Em Progresso
            </span>
            <span class="text-xs px-2 py-0.5 bg-amber-950 text-amber-400 rounded-full font-mono" id="count-progresso">1</span>
          </div>
          <div class="flex-1 space-y-2 overflow-y-auto pr-1" id="list-progresso">
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">Sprint 2</span>
              <h4 class="text-xs font-semibold text-white">Fila FIFO de Atendimento</h4>
              <p class="text-[11px] text-slate-400">Algoritmo em pseudocódigo e teste interativo em JS.</p>
              <div class="flex justify-between items-center text-[10px] text-slate-500 pt-2 border-t border-slate-800">
                <span>Prazo: Hoje</span>
                <button onclick="moverTarefa(this, 'concluido')" class="hover:text-emerald-400">Concluir &checkmark;</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Concluído -->
        <div class="bg-slate-950/60 border border-slate-800 rounded-xl p-3 flex flex-col h-[500px]">
          <div class="flex items-center justify-between mb-3 px-1">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400"></span> Concluído
            </span>
            <span class="text-xs px-2 py-0.5 bg-emerald-950 text-emerald-400 rounded-full font-mono" id="count-concluido">2</span>
          </div>
          <div class="flex-1 space-y-2 overflow-y-auto pr-1" id="list-concluido">
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2 opacity-80">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Sprint 1</span>
              <h4 class="text-xs font-semibold text-white line-through">Diagrama UML de Casos de Uso</h4>
              <p class="text-[11px] text-slate-400">Mapeamento dos atores Secretária e Médico com relac. include.</p>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-3 rounded-lg shadow-sm hover:border-slate-700 transition space-y-2 opacity-80">
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Sprint 1</span>
              <h4 class="text-xs font-semibold text-white line-through">Especificação de Requisitos</h4>
              <p class="text-[11px] text-slate-400">Documento base com regras funcionais aprovadas.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 2: Código Executável em Python -->
    <section id="sec-passo2" class="tab-content hidden space-y-6">
      <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
          <div>
            <h3 class="text-lg font-bold text-white flex items-center space-x-2">
              <i class="fa-brands fa-python text-emerald-400 text-xl"></i>
              <span>Passo 2: Código Python Executável (`clinica_vida.py`)</span>
            </h3>
            <p class="text-xs text-slate-400">Gerenciamento de pacientes utilizando listas e dicionários com tratamento rigoroso de erros.</p>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="baixarCodigoPython()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white hover:bg-emerald-500 transition flex items-center space-x-1.5">
              <i class="fa-solid fa-download"></i>
              <span>Baixar Arquivo .py</span>
            </button>
          </div>
        </div>

        <!-- Terminal Simulator -->
        <div class="bg-black border border-slate-800 rounded-xl p-4 font-mono text-xs text-emerald-400 space-y-3 shadow-inner">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 text-slate-500 text-[11px]">
            <span class="flex items-center gap-2"><i class="fa-solid fa-terminal"></i> Terminal Interativo - Python 3.12</span>
            <span>Status: Pronto para teste</span>
          </div>

          <div id="terminal-output" class="h-64 overflow-y-auto space-y-1 text-slate-300 pr-2">
            <p class="text-slate-500">--- CLÍNICA VIDA+ SISTEMA DE PACIENTES INITIALIZED ---</p>
            <p class="text-slate-500">Dados demonstrativos carregados: 3 pacientes na memória.</p>
            <p class="text-amber-400">Digite uma opção do menu no campo abaixo:</p>
          </div>

          <form id="terminal-form" onsubmit="executarComandoPython(event)" class="flex items-center space-x-2 pt-2 border-t border-slate-800">
            <span class="text-emerald-400 font-bold">&gt;</span>
            <input type="text" id="terminal-input" placeholder="Escolha (1-5) ou aperte enter..." class="flex-1 bg-transparent text-white focus:outline-none font-mono text-xs">
            <button type="submit" class="px-3 py-1 bg-emerald-600/30 text-emerald-400 border border-emerald-500/30 rounded text-xs hover:bg-emerald-600/50">Enviar</button>
          </form>
        </div>

        <!-- Python Code Display -->
        <div class="space-y-2">
          <h4 class="text-sm font-semibold text-slate-300">Código-Fonte Completo (`clinica_vida.py`):</h4>
          <pre class="bg-slate-900 border border-slate-800 rounded-xl p-4 text-xs text-slate-300 overflow-x-auto max-h-96"><code># clinica_vida.py
# Sistema de Gestão de Pacientes - Clínica Vida+

def exibir_menu():
    print("\n" + "="*35)
    print("      CLÍNICA VIDA+ - MENU")
    print("="*35)
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente pelo nome")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    print("="*35)

def cadastrar_paciente(pacientes):
    print("\n--- CADASTRO DE PACIENTE ---")
    nome = input("Digite o nome completo do paciente: ").strip()
    while not nome:
        print("Erro: O nome não pode estar em branco.")
        nome = input("Digite o nome completo do paciente: ").strip()
        
    while True:
        try:
            idade = int(input("Digite a idade do paciente: "))
            if idade < 0 or idade > 130:
                print("Erro: Digite uma idade válida (0 a 130).")
                continue
            break
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro para a idade.")
            
    telefone = input("Digite o telefone do paciente (ex: 41999998888): ").strip()
    while not telefone:
        print("Erro: O telefone não pode estar em branco.")
        telefone = input("Digite o telefone do paciente: ").strip()
        
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print(f"\nSucesso: Paciente '{nome}' cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    print("\n--- ESTATÍSTICAS DOS PACIENTES ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado no sistema até o momento.")
        return

    total = len(pacientes)
    soma_idades = sum(p["idade"] for p in pacientes)
    idade_media = soma_idades / total
    
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    
    print(f"Total de pacientes cadastrados : {total}")
    print(f"Idade média dos pacientes       : {idade_media:.1f} anos")
    print(f"Paciente mais novo             : {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho            : {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    print("\n--- BUSCA DE PACIENTE ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado para realizar a busca.")
        return
        
    termo = input("Digite o nome (ou parte do nome) do paciente: ").strip().lower()
    encontrados = [p for p in pacientes if termo in p["nome"].lower()]
    
    if encontrados:
        print(f"\nForam encontrados {len(encontrados)} paciente(s):")
        for p in encontrados:
            print(f"- Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
    else:
        print(f"Aviso: Nenhum paciente encontrado com o nome '{termo}'.")

def listar_pacientes(pacientes):
    print("\n--- LISTA COMPLETA DE PACIENTES ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado na base de dados.")
        return
        
    for idx, p in enumerate(pacientes, start=1):
        print(f"{idx}. {p['nome']} | {p['idade']} anos | Tel: {p['telefone']}")

def main():
    pacientes = []
    
    # Dados demonstrativos iniciais
    pacientes.append({"nome": "Ana Silva", "idade": 28, "telefone": "41991112222"})
    pacientes.append({"nome": "Carlos Eduardo", "idade": 65, "telefone": "41988887777"})
    pacientes.append({"nome": "Beatriz Souza", "idade": 12, "telefone": "41977776666"})

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("\nEncerrando o sistema da Clínica Vida+. Até logo!")
            break
        else:
            print("\nErro: Opção inválida! Escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()</code></pre>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 3: Lógica Proposicional e Tabelas-Verdade -->
    <section id="sec-passo3" class="tab-content hidden space-y-6">
      <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-6">
        <div>
          <h3 class="text-lg font-bold text-white">Passo 3: Lógica Proposicional e Liberação de Consultas</h3>
          <p class="text-xs text-slate-400">Validação formal das regras de negócio de atendimento via álgebra booleana (16 combinações).</p>
        </div>

        <!-- Definições das Proposições -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
          <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
            <span class="font-bold text-sky-400 font-mono">A</span> = Tem agendamento
          </div>
          <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
            <span class="font-bold text-sky-400 font-mono">B</span> = Documentos válidos
          </div>
          <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
            <span class="font-bold text-sky-400 font-mono">C</span> = Médico disponível
          </div>
          <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
            <span class="font-bold text-sky-400 font-mono">D</span> = Pagamentos em dia
          </div>
        </div>

        <!-- Expressões Lógicas -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl space-y-1">
            <span class="text-xs text-slate-400 font-semibold uppercase">Consulta Normal</span>
            <div class="font-mono text-emerald-400 font-bold text-sm">(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)</div>
            <p class="text-[11px] text-slate-400 pt-1">Atendimento liberado em <strong>3 de 16</strong> combinações.</p>
          </div>
          <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-xl space-y-1">
            <span class="text-xs text-slate-400 font-semibold uppercase">Emergência</span>
            <div class="font-mono text-amber-400 font-bold text-sm">C ∧ (B ∨ D)</div>
            <p class="text-[11px] text-slate-400 pt-1">Atendimento liberado em <strong>6 de 16</strong> combinações.</p>
          </div>
        </div>

        <!-- Destaque para o caso específico -->
        <div class="bg-sky-950/40 border border-sky-500/30 p-4 rounded-xl space-y-2">
          <h4 class="text-xs font-bold text-sky-400 uppercase tracking-wider flex items-center gap-2">
            <i class="fa-solid fa-magnifying-glass font-bold"></i> Análise do Caso Solicitado: A = F, B = V, C = V, D = F
          </h4>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
            <div class="space-y-1">
              <span class="font-semibold text-white">Consulta Normal: BLOQUEADA (F)</span>
              <p class="text-slate-300 text-[11px] leading-relaxed">
                <code class="text-rose-400">(F ∧ V ∧ V) ∨ (V ∧ V ∧ F) = F ∨ F = F</code>.<br>
                Sem agendamento (A=F) e sem pagamentos em dia (D=F), a consulta normal não atende a nenhuma das condições de liberação.
              </p>
            </div>
            <div class="space-y-1">
              <span class="font-semibold text-white">Emergência: LIBERADA (V)</span>
              <p class="text-slate-300 text-[11px] leading-relaxed">
                <code class="text-emerald-400">V ∧ (V ∨ F) = V ∧ V = V</code>.<br>
                Há médico disponível (C=V) e documentos válidos (B=V), garantindo atendimento imediato independente de pendência financeira ou agendamento.
              </p>
            </div>
          </div>
        </div>

        <!-- Tabela Verdade Unificada de 16 linhas -->
        <div class="overflow-x-auto rounded-xl border border-slate-800">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-slate-900 text-slate-400 uppercase font-mono text-[11px]">
              <tr>
                <th class="px-3 py-2 text-center">#</th>
                <th class="px-3 py-2 text-center">A</th>
                <th class="px-3 py-2 text-center">B</th>
                <th class="px-3 py-2 text-center">C</th>
                <th class="px-3 py-2 text-center">D</th>
                <th class="px-3 py-2 text-center bg-slate-800/50">Consulta Normal</th>
                <th class="px-3 py-2 text-center bg-slate-800/50">Emergência</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800/60 font-mono text-center">
              <tr class="hover:bg-slate-900/50"><td>1</td><td>V</td><td>V</td><td>V</td><td>V</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-slate-900/50"><td>2</td><td>V</td><td>V</td><td>V</td><td>F</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-slate-900/50"><td>3</td><td>V</td><td>V</td><td>F</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>4</td><td>V</td><td>V</td><td>F</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>5</td><td>V</td><td>F</td><td>V</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-slate-900/50"><td>6</td><td>V</td><td>F</td><td>V</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>7</td><td>V</td><td>F</td><td>F</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>8</td><td>V</td><td>F</td><td>F</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>9</td><td>F</td><td>V</td><td>V</td><td>V</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-sky-950/60 bg-sky-950/20 font-bold border-l-2 border-sky-400"><td>10</td><td>F</td><td>V</td><td>V</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-slate-900/50"><td>11</td><td>F</td><td>V</td><td>F</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>12</td><td>F</td><td>V</td><td>F</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>13</td><td>F</td><td>F</td><td>V</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-emerald-400 font-bold bg-slate-900/30">V</td></tr>
              <tr class="hover:bg-slate-900/50"><td>14</td><td>F</td><td>F</td><td>V</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>15</td><td>F</td><td>F</td><td>F</td><td>V</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
              <tr class="hover:bg-slate-900/50"><td>16</td><td>F</td><td>F</td><td>F</td><td>F</td><td class="text-rose-400 bg-slate-900/30">F</td><td class="text-rose-400 bg-slate-900/30">F</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 4: Algoritmo Fila FIFO -->
    <section id="sec-passo4" class="tab-content hidden space-y-6">
      <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-6">
        <div>
          <h3 class="text-lg font-bold text-white">Passo 4: Algoritmo e Estrutura de Fila FIFO</h3>
          <p class="text-xs text-slate-400">Implementação sequencial Primeiro a Entrar, Primeiro a Sair (First-In, First-Out).</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Pseudocódigo -->
          <div class="space-y-2">
            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Algoritmo em Pseudocódigo:</h4>
            <pre class="bg-slate-900 border border-slate-800 rounded-xl p-4 text-xs text-emerald-400 overflow-x-auto"><code>ALGORITMO GestaoFilaClinicaVida
    ESTRUTURA Paciente
        NOME: TEXTO
        CPF: TEXTO
    FIM_ESTRUTURA

    VARIAVEIS
        filaAtendimento: FILA DE Paciente
        p1, p2, p3, atendido: Paciente
    
    INICIO
        CRIAR_FILA_VAZIA(filaAtendimento)
        
        // Enfileira 3 pacientes
        p1.NOME <- "Maria Oliveira"
        p1.CPF  <- "111.222.333-44"
        ENFILEIRAR(filaAtendimento, p1)
        
        p2.NOME <- "João Santos"
        p2.CPF  <- "555.666.777-88"
        ENFILEIRAR(filaAtendimento, p2)
        
        p3.NOME <- "Lucia Lima"
        p3.CPF  <- "999.000.111-22"
        ENFILEIRAR(filaAtendimento, p3)
        
        // Remove o primeiro para atendimento
        atendido <- DESENFILEIRAR(filaAtendimento)
        ESCREVER("Atendendo agora: ", atendido.NOME)
        
        // Exibe os 2 restantes na ordem estrita
        ESCREVER("--- PACIENTES RESTANTES NA FILA ---")
        PARA CADA pac EM filaAtendimento FAÇA
            ESCREVER("Paciente: ", pac.NOME, " | CPF: ", pac.CPF)
        FIM_PARA
FIM_ALGORITMO</code></pre>
          </div>

          <!-- Simulador Visual Interativo da Fila -->
          <div class="bg-slate-900 border border-slate-800 p-5 rounded-xl space-y-4 flex flex-col justify-between">
            <div>
              <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider mb-2">Simulador Visual da Fila FIFO</h4>
              <p class="text-xs text-slate-400">Inicie com 3 pacientes, chame o próximo para atendimento e observe os restantes preservarem a ordem.</p>
            </div>

            <div id="fifo-visual-container" class="space-y-2 py-2">
              <!-- Renderizado via JS -->
            </div>

            <div class="flex items-center space-x-2 pt-3 border-t border-slate-800">
              <button onclick="chamarProximoFila()" class="flex-1 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition flex items-center justify-center space-x-2">
                <i class="fa-solid fa-user-check"></i>
                <span>Chamar Próximo (Desenfileirar)</span>
              </button>
              <button onclick="resetarFilaDemo()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs transition">
                <i class="fa-solid fa-rotate-right"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SEÇÃO 5: Diagrama de Casos de Uso UML -->
    <section id="sec-passo5" class="tab-content hidden space-y-6">
      <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6 space-y-6">
        <div>
          <h3 class="text-lg font-bold text-white">Passo 5: Diagrama UML de Casos de Uso</h3>
          <p class="text-xs text-slate-400">Mapeamento de Atores (Secretária e Médico) e Inclusões Obrigatórias (&lt;&lt;include&gt;&gt;).</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Especificação dos Atores -->
          <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl space-y-3">
            <h4 class="text-xs font-bold text-sky-400 uppercase tracking-wider">Atores & Papéis</h4>
            <div class="space-y-3 text-xs">
              <div class="border-b border-slate-800 pb-2">
                <span class="font-bold text-white flex items-center gap-1.5"><i class="fa-solid fa-user-gear text-sky-400"></i> Secretária</span>
                <p class="text-slate-400 text-[11px] mt-1">Cadastra paciente, agenda consulta, confirma consulta e cancela consulta.</p>
              </div>
              <div>
                <span class="font-bold text-white flex items-center gap-1.5"><i class="fa-solid fa-user-doctor text-emerald-400"></i> Médico</span>
                <p class="text-slate-400 text-[11px] mt-1">Cancela consulta e gera receita médica.</p>
              </div>
            </div>
          </div>

          <!-- Representação Visual do Diagrama -->
          <div class="md:col-span-2 bg-slate-900 border border-slate-800 p-5 rounded-xl space-y-4">
            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider">Limites do Sistema & Relacionamentos</h4>
            <div class="border-2 border-dashed border-slate-700 p-4 rounded-xl relative bg-slate-950/50 space-y-3">
              <span class="absolute -top-3 left-4 bg-slate-800 text-[10px] text-slate-300 px-2 py-0.5 rounded font-mono">Boundary: Sistema Clínica Vida+</span>
              
              <div class="grid grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-900 p-2.5 rounded border border-slate-800 text-center text-slate-200">
                  Cadastrar Paciente
                </div>
                <div class="bg-slate-900 p-2.5 rounded border border-slate-800 text-center text-slate-200">
                  Cancelar Consulta
                </div>
                <div class="bg-sky-950/40 p-2.5 rounded border border-sky-500/30 text-center text-sky-300">
                  Agendar Consulta
                  <span class="block text-[9px] text-sky-400 font-mono mt-0.5">&lt;&lt;include&gt;&gt; Verificar Cadastro</span>
                </div>
                <div class="bg-sky-950/40 p-2.5 rounded border border-sky-500/30 text-center text-sky-300">
                  Confirmar Consulta
                  <span class="block text-[9px] text-sky-400 font-mono mt-0.5">&lt;&lt;include&gt;&gt; Verificar Cadastro</span>
                </div>
                <div class="col-span-2 bg-emerald-950/40 p-2.5 rounded border border-emerald-500/30 text-center text-emerald-300">
                  Gerar Receita
                  <span class="block text-[9px] text-emerald-400 font-mono mt-0.5">&lt;&lt;include&gt;&gt; Imprimir Receita</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Modal de Relatório da Sprint -->
    <div id="modal-relatorio" class="fixed inset-0 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4 z-50 no-print">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-2xl w-full p-6 space-y-4 shadow-2xl">
        <div class="flex justify-between items-center border-b border-slate-800 pb-3">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-file-lines text-sky-400"></i> Relatório de Desempenho da Sprint 2
          </h3>
          <button onclick="fecharRelatorioSprint()" class="text-slate-400 hover:text-white">&times;</button>
        </div>
        <div class="space-y-3 text-xs text-slate-300 max-h-96 overflow-y-auto">
          <div>
            <h4 class="font-bold text-emerald-400">Resultados Alcançados:</h4>
            <p>Conclusão completa das tabelas-verdade de 16 combinações e validação do módulo Python com 100% de cobertura contra exceções.</p>
          </div>
          <div>
            <h4 class="font-bold text-amber-400">Desafios Encontrados:</h4>
            <p>Modelagem da ambiguidade em consultas normais sem agendamento. Resolvido adicionando a cláusula complementar de pagamento regular.</p>
          </div>
          <div>
            <h4 class="font-bold text-sky-400">Pontos Positivos & Melhorias:</h4>
            <p>Trabalho transdisciplinar integrado entre as disciplinas de Lógica e Estrutura de Dados.</p>
          </div>
        </div>
        <div class="pt-3 border-t border-slate-800 flex justify-end">
          <button onclick="fecharRelatorioSprint()" class="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold">Fechar</button>
        </div>
      </div>
    </div>

  </main>

  <!-- Footer Rodapé -->
  <footer class="bg-slate-950 border-t border-slate-800 py-4 text-center text-xs text-slate-500 no-print">
    <p>Clínica Vida+ &copy; 2026 - Todos os dados apresentados são estritamente fictícios e para fins acadêmicos.</p>
  </footer>

  <!-- Script Logic -->
  <script>
    // Tab Navigation
    function setTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(el => {
        el.classList.remove('active', 'bg-sky-600', 'text-white');
        el.classList.add('text-slate-400');
      });
      
      document.getElementById('sec-' + tabId).classList.remove('hidden');
      const activeBtn = document.getElementById('tab-' + tabId);
      activeBtn.classList.add('active');
      activeBtn.classList.remove('text-slate-400');
    }

    // Python File Download
    function baixarCodigoPython() {
      const code = `# clinica_vida.py
# Sistema de Gestão de Pacientes - Clínica Vida+

def exibir_menu():
    print("\\n" + "="*35)
    print("      CLÍNICA VIDA+ - MENU")
    print("="*35)
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente pelo nome")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    print("="*35)

def cadastrar_paciente(pacientes):
    print("\\n--- CADASTRO DE PACIENTE ---")
    nome = input("Digite o nome completo do paciente: ").strip()
    while not nome:
        print("Erro: O nome não pode estar em branco.")
        nome = input("Digite o nome completo do paciente: ").strip()
        
    while True:
        try:
            idade = int(input("Digite a idade do paciente: "))
            if idade < 0 or idade > 130:
                print("Erro: Digite uma idade válida (0 a 130).")
                continue
            break
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro para a idade.")
            
    telefone = input("Digite o telefone do paciente (ex: 41999998888): ").strip()
    while not telefone:
        print("Erro: O telefone não pode estar em branco.")
        telefone = input("Digite o telefone do paciente: ").strip()
        
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print(f"\\nSucesso: Paciente '{nome}' cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    print("\\n--- ESTATÍSTICAS DOS PACIENTES ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado no sistema até o momento.")
        return

    total = len(pacientes)
    soma_idades = sum(p["idade"] for p in pacientes)
    idade_media = soma_idades / total
    
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])
    
    print(f"Total de pacientes cadastrados : {total}")
    print(f"Idade média dos pacientes       : {idade_media:.1f} anos")
    print(f"Paciente mais novo             : {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho            : {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente(pacientes):
    print("\\n--- BUSCA DE PACIENTE ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado para realizar a busca.")
        return
        
    termo = input("Digite o nome (ou parte do nome) do paciente: ").strip().lower()
    encontrados = [p for p in pacientes if termo in p["nome"].lower()]
    
    if encontrados:
        print(f"\\nForam encontrados {len(encontrados)} paciente(s):")
        for p in encontrados:
            print(f"- Nome: {p['nome']} | Idade: {p['idade']} | Tel: {p['telefone']}")
    else:
        print(f"Aviso: Nenhum paciente encontrado com o nome '{termo}'.")

def listar_pacientes(pacientes):
    print("\\n--- LISTA COMPLETA DE PACIENTES ---")
    if not pacientes:
        print("Aviso: Nenhum paciente cadastrado na base de dados.")
        return
        
    for idx, p in enumerate(pacientes, start=1):
        print(f"{idx}. {p['nome']} | {p['idade']} anos | Tel: {p['telefone']}")

def main():
    pacientes = []
    
    # Dados demonstrativos iniciais
    pacientes.append({"nome": "Ana Silva", "idade": 28, "telefone": "41991112222"})
    pacientes.append({"nome": "Carlos Eduardo", "idade": 65, "telefone": "41988887777"})
    pacientes.append({"nome": "Beatriz Souza", "idade": 12, "telefone": "41977776666"})

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            cadastrar_paciente(pacientes)
        elif opcao == "2":
            ver_estatisticas(pacientes)
        elif opcao == "3":
            buscar_paciente(pacientes)
        elif opcao == "4":
            listar_pacientes(pacientes)
        elif opcao == "5":
            print("\\nEncerrando o sistema da Clínica Vida+. Até logo!")
            break
        else:
            print("\\nErro: Opção inválida! Escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()
`;
      const blob = new Blob([code], { type: 'text/python' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'clinica_vida.py';
      a.click();
      URL.revokeObjectURL(url);
    }

    // Terminal Emulator state
    let demoPacientes = [
      { nome: "Ana Silva", idade: 28, telefone: "41991112222" },
      { nome: "Carlos Eduardo", idade: 65, telefone: "41988887777" },
      { nome: "Beatriz Souza", idade: 12, telefone: "41977776666" }
    ];

    function executarComandoPython(e) {
      e.preventDefault();
      const input = document.getElementById('terminal-input');
      const out = document.getElementById('terminal-output');
      const val = input.value.trim();
      input.value = '';

      if (!val) return;

      out.innerHTML += `<p class="text-sky-400 font-bold">&gt; ${val}</p>`;

      if (val === '1') {
        out.innerHTML += `<p class="text-amber-400">[Simulação] Paciente 'Marcos Lima' (45 anos) cadastrado com sucesso!</p>`;
        demoPacientes.push({ nome: "Marcos Lima", idade: 45, telefone: "41999990000" });
      } else if (val === '2') {
        const total = demoPacientes.length;
        const media = (demoPacientes.reduce((acc, p) => acc + p.idade, 0) / total).toFixed(1);
        const novo = [...demoPacientes].sort((a,b) => a.idade - b.idade)[0];
        const velho = [...demoPacientes].sort((a,b) => b.idade - a.idade)[0];
        out.innerHTML += `<p class="text-emerald-300">Total: ${total} | Média: ${media} anos<br>Mais Novo: ${novo.nome} (${novo.idade}) | Mais Velho: ${velho.nome} (${velho.idade})</p>`;
      } else if (val === '3') {
        out.innerHTML += `<p class="text-slate-300">Buscando 'Ana': Encontrado 1 registro (Ana Silva - 28 anos)</p>`;
      } else if (val === '4') {
        let listaStr = demoPacientes.map((p, i) => `${i+1}. ${p.nome} (${p.idade}a) - Tel: ${p.telefone}`).join('<br>');
        out.innerHTML += `<p class="text-slate-300">${listaStr}</p>`;
      } else if (val === '5') {
        out.innerHTML += `<p class="text-rose-400">Sistema encerrado com sucesso.</p>`;
      } else {
        out.innerHTML += `<p class="text-rose-400">Erro: Opção inválida! Escolha de 1 a 5.</p>`;
      }

      out.scrollTop = out.scrollHeight;
    }

    // Fila FIFO state
    let filaEstado = [
      { nome: "Maria Oliveira", cpf: "111.222.333-44" },
      { nome: "João Santos", cpf: "555.666.777-88" },
      { nome: "Lucia Lima", cpf: "999.000.111-22" }
    ];

    function renderFila() {
      const container = document.getElementById('fifo-visual-container');
      if (filaEstado.length === 0) {
        container.innerHTML = `<div class="p-3 bg-slate-950 border border-slate-800 rounded-lg text-center text-xs text-slate-500">A fila está vazia. Todos os pacientes foram atendidos!</div>`;
        return;
      }

      container.innerHTML = filaEstado.map((p, idx) => `
        <div class="flex items-center justify-between p-3 ${idx === 0 ? 'bg-emerald-950/40 border-emerald-500/40' : 'bg-slate-950 border-slate-800'} border rounded-lg text-xs transition">
          <div class="flex items-center space-x-3">
            <span class="w-5 h-5 rounded-full ${idx === 0 ? 'bg-emerald-500 text-white' : 'bg-slate-800 text-slate-400'} flex items-center justify-center font-bold text-[10px]">${idx + 1}</span>
            <div>
              <span class="font-bold text-white block">${p.nome}</span>
              <span class="text-[10px] text-slate-400 font-mono">CPF: ${p.cpf}</span>
            </div>
          </div>
          ${idx === 0 ? '<span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 uppercase">PRÓXIMO A ATENDER</span>' : '<span class="text-[10px] text-slate-500">Aguardando</span>'}
        </div>
      `).join('');
    }

    function chamarProximoFila() {
      if (filaEstado.length > 0) {
        const atendido = filaEstado.shift();
        alert(`Atendendo agora: ${atendido.nome} (CPF: ${atendido.cpf})`);
        renderFila();
      }
    }

    function resetarFilaDemo() {
      filaEstado = [
        { nome: "Maria Oliveira", cpf: "111.222.333-44" },
        { nome: "João Santos", cpf: "555.666.777-88" },
        { nome: "Lucia Lima", cpf: "999.000.111-22" }
      ];
      renderFila();
    }

    // Modal Handlers
    function mostrarRelatorioSprint() {
      document.getElementById('modal-relatorio').classList.remove('hidden');
      document.getElementById('modal-relatorio').classList.add('flex');
    }

    function fecharRelatorioSprint() {
      document.getElementById('modal-relatorio').classList.add('hidden');
      document.getElementById('modal-relatorio').classList.remove('flex');
    }

    function mostrarGuiaTrelloReal() {
      alert("Para criar no Trello Real:\n1. Acesse trello.com\n2. Crie um quadro chamado 'Clínica Vida+'\n3. Adicione as listas: Backlog, Sprint Atual, Em Progresso e Concluído.\n4. Replique as tarefas exibidas nesta seção.");
    }

    function moverTarefa(btn, destino) {
      const card = btn.closest('.bg-slate-900');
      document.getElementById('list-' + destino).appendChild(card);
    }

    function exportarRelatorioCompleto() {
      window.print();
    }

    // Init
    document.addEventListener('DOMContentLoaded', () => {
      renderFila();
    });
  </script>
</body>
</html>
