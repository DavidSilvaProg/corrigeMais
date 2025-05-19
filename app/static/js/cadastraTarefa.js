function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.classList.toggle('show');
}

  let questionCount = 0;

  function addQuestion() {
    questionCount++;
    const tipo = document.getElementById("tipoQuestao").value;
    const container = document.getElementById("questions-container");

    const questionDiv = document.createElement("div");
    questionDiv.className = "question";
    questionDiv.dataset.tipo = tipo;
    questionDiv.dataset.qid = questionCount; // Identificador interno único

    const tipoTexto = tipo === "unica" ? "Resposta Única" : "Múltipla Escolha";

    let html = `
      <label class="question-label">Enunciado da Questão (${tipoTexto}):</label>
      <input type="text" name="question_${questionCount}" required>
    `;

    if (tipo === "multipla") {
      html += `
        <div class="options">
          <label>Opções:</label><br>
          ${createOptionInput(tipo, questionCount)}
          ${createOptionInput(tipo, questionCount)}
        </div>
        <button type="button" onclick="addOption(this, '${tipo}', ${questionCount})">Adicionar Opção</button>
      `;
    }

    html += `<button type="button" class="remove-btn" onclick="removeQuestion(this)">Remover Questão</button>`;

    questionDiv.innerHTML = html;
    container.appendChild(questionDiv);

    atualizarNumeracao();
  }

  function createOptionInput(tipo, qId) {
    const inputType = tipo === 'unica' ? 'radio' : 'checkbox';
    return `
      <div>
        <input type="${inputType}" disabled>
        <input type="text" name="question_${qId}_option[]" required>
      </div>`;
  }

  function addOption(button, tipo, qId) {
    const optionsDiv = button.previousElementSibling;
    const inputType = tipo === 'unica' ? 'radio' : 'checkbox';

    const optionDiv = document.createElement("div");
    optionDiv.innerHTML = `
      <input type="${inputType}" disabled>
      <input type="text" name="question_${qId}_option[]" required>
    `;

    optionsDiv.appendChild(optionDiv);
  }

  function removeQuestion(button) {
    const questionDiv = button.parentElement;
    questionDiv.remove();
    atualizarNumeracao();
  }

  function atualizarNumeracao() {
    const questions = document.querySelectorAll(".question");
    questions.forEach((q, index) => {
      const tipo = q.dataset.tipo;
      const tipoTexto = tipo === "unica" ? "Resposta Única" : "Múltipla Escolha";

      const label = q.querySelector(".question-label");
      label.textContent = `Enunciado da Questão ${index + 1} (${tipoTexto}):`;
    });
  }

  function submitForm() {
    alert("Questionário salvo (simulação). Aqui você pode enviar os dados com JavaScript para o back-end.");
  }