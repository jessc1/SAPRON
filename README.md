# SAPRON
> API que retorna a agenda de um anfitrião, o usuário da API no qual irá adicionar, 
deletar, visualizar e criar um hóspede na aplicação.


# Tecnologias:
* Django  
* Django Rest Framework  
* Postgresql

Para o desenvolvimento da API, criei o modelo Agenda com os campos: hóspede no qual
irá armazenar o nome do hóspede. O campo checkin será adicionado no momento em que
as informações do usuário forem salvas, o checkin que irá armazenar a data de saída
do hóspede e o campo limpeza que salva a data de limpeza. Criei o modelo serializer, 
no qual vai converter os objetos python em formato json.
Usei Class Based API views e generic views: ListAPIView  para listar os hóspedes;
                                              RetrieveAPIView para visualizar um hóspede;
                                              RetrieveUpdateAPIView para atualizar e 
                                              DestroyAPIView para deletar um hóspede.
Criei as urls para cada view : a url 'agenda' lista todos os hóspedes da API.
Para visualizar um hóspede específico é necessario adicionar o id: agenda/<int:id>/
É criado um novo hóspede em agenda/create, Atualiza em agenda/update/<int:id>/ e deleta 
com agenda/delete/<int:id>.
Adicionei o campo Search para consultar um hóspede por nome ou id e um filtro para ordenação 
do checkin por ordem crescente ou decrescente; paginação onde cada página terá um total de 10 
hóspedes por página.
O usuário precisa ter feito o log in para ter acesso a API, caso contrário, irá aparecer o 
status 403 "detail": "Authentication credentials were not provided.".
  
  
                                              
                                              
                                            
                                             
  
 

