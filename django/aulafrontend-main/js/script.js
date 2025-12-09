// window.onload = function(){
//     alert("Seja bem-vindo à Jornada Viagens! ✈✈");
// }

// Função que captura os dados do formulário e exibe via document.write
function exibirDados() {
    // Captura os valores dos inputs
    let nome =  document.getElementById('nome').value;
    let tel = document.getElementById('movel').value;
    let email = document.getElementById('correio').value;

    // Usando document.write para exibir os dados na página
    document.write('<h2>Dados Recebidos:</h2>');
    document.write('<p><strong>Nome:</strong> ' + nome + '</p>');
    document.write('<p><strong>Telefone:</strong> ' + tel + '</p>');
    document.write('<p><strong>E-mail:</strong> ' + email + '</p>');
}