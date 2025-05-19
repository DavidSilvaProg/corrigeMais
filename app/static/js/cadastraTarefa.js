let questionCount = 0;

function addQuestion() {
    questionCount++;
    const container = document.getElementById("questions-container");

    const questionDiv = document.createElement("div");
    questionDiv.className = "question";
    questionDiv.innerHTML = `
        <label>Enunciado da Questão ${questionCount}:</label>
        <input type="text" name="question_${questionCount}" required>
        <div class="options">
            <label>Opções:</label><br>
            <input type="text" name="question_${questionCount}_option[]" required>
            <input type="text" name="question_${questionCount}_option[]" required>
        </div>
        <button type="button" onclick="addOption(this)">Adicionar Opção</button>
        <button type="button" class="remove-btn" onclick="removeQuestion(this)">Remover Questão</button>
    `;

    container.appendChild(questionDiv);
}

function addOption(button) {
    const optionsDiv = button.previousElementSibling;
    const input = document.createElement("input");
    input.type = "text";
    input.name = optionsDiv.querySelector("input").name;
    input.required = true;
    optionsDiv.appendChild(input);
}

function removeQuestion(button) {
    const questionDiv = button.parentElement;
    questionDiv.remove();
}

function submitForm() {
    alert("Questionário salvo (simulação). Aqui você pode enviar os dados com JavaScript para o back-end.");
    // Aqui você pode usar fetch/AJAX para enviar os dados.
}