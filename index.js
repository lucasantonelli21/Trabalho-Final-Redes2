document.addEventListener("DOMContentLoaded", function() {
    carregarUsers();
});

function carregarUsers() {
    fetch('http://localhost:5000/users')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#users-table tbody");
            tbody.innerHTML = "";
            data.forEach(usuario => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${usuario[0]}</td>
                    <td>${usuario[1]}</td>
                    <td>${usuario[2]}</td>
                    <td>${usuario[3]}</td>
                    <td>
                        <button onclick="atualizarUser(${usuario[0]})">Atualizar</button>
                        <button id="del" onclick="deletarUser(${usuario[0]})">Deletar</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        });
}

function criarUser() {
    const user = document.getElementById("usuario").value;
    const nomeCompleto = document.getElementById("nomeCompleto").value;
    const cpf = document.getElementById("cpf").value;

    fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user, nomeCompleto, cpf })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensagem);
        carregarUsers();
    });
}

function atualizarUser(id) {
    const user = prompt("Novo user do usuario:");
    const nomeCompleto = prompt("Novo Nome do usuario:");
    const cpf = prompt("Novo cpf:");

    fetch(`http://localhost:5000/users/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user, nomeCompleto, cpf })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensagem);
        carregarUsers();
    });
}

function deletarUser(id) {
    fetch(`http://localhost:5000/users/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensagem);
        carregarUsers();
    });
}
