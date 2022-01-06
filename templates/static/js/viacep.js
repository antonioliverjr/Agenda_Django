$(function(){
    function consultaCep(){
        var cep = $("#id_cep").val();
        if (cep.length === 8){
            var url = "https://viacep.com.br/ws/" + cep + "/json/";
            $.getJSON(url, function(response){
                if (!response.erro){
                    console.log(response);
                    $("#id_logradouro").val(response.logradouro);
                    $("#id_bairro").val(response.bairro);
                    $("#id_localidade").val(response.localidade);
                    $("#id_uf").val(response.uf);
                    $("#id_complemento").val(response.complemento);
                }else{
                    alert("Informe um cep valido!")
                }
            })
        }else{
            alert("Campo CEP deve conter 8 digitos (0~9)!")
        }
        
    }
    
    $("#id_cep").on("focusout", function(){
        consultaCep()
    });
})