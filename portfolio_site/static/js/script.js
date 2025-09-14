const form = document.getElementById('formContato');
form.addEventListener('submit', function (event) {
    event.preventDefault();        const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();
    if (!nome || !email || !mensagem) {
        alert('Por favor, preencha todos os campos antes de enviar.');
        return;
        }
    else {
        alert('Formulário enviado com sucesso!');
        form.reset();
    }
});