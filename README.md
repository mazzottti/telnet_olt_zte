# telnet_olt_zte
Um Telnet simples em python para automatizar alguns comandos nas olts zte c300

Essa função usa a lib telnetlib para executar um telnet lendo seu retorno e escrevendo alguns comandos, a telnetlib só aceita dados em byte, 
por isso vai encontrar alguns b'' ou encode('utf-8') no codigo.

O codigo foi feito para equipamentos zte, mas pode ser adequado a qualquer fabricante, basta mudar o retorno de login, ex:
ao conectar na zte ela pede o usuario dessa forma "Username:", caso seu equipamento retorne outra informação, altere a linha 7 (tn.read_until(b"Username:"))
o mesmo para a senha na linha 9 e prompt na 11. 



Para que a função telnet funcione, vai precisar preencher alguns dados;

host = Ip da olt,
username = Usuario da olt,
password = Senha da olt,
lista_comando = Os comandos que precisa rodar em formato de lista ['x','y','etc'],


não tem muito o que explicar, é bem simples.
