
# def isValid(s='()'):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dct={'(':')','{':'}','[':']'}
#         for x in s:
#             Found=False
#             for i in x:
#                 if i in dct.keys() and dct[i] in dct.values():
                     
                     
                
# isValid()

# ;
#      select a.name,j.name,count(j.name) as Jami from kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by a.name,j.name
#     order by j.name desc;

#     select a.name,j.name,count(j.name) as jami from  kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by a.name,j.name
#     order by jami;

#     select j.name, count(j.name) as jami from kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by j.name
#     order by jami desc limit 1;



#      select a.name,sum(sold_count) as summ from kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by a.name
#     order by summ;

#      select a.name,sum(sold_count) as summ from kitob as k
#     ->     join author as a on k.a_id=a.id
#     ->     join janr as j on k.j_id=j.id
#     ->     group a.name
#     -> orde by summ;


#     select a.name ,j.name,count(j.name)  as jami from kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by a.name,j.name
#     order by jami;

    
# mysql>  select a.name ,j.name,count(j.name)  as jami from kitob as k
#     join author as a on k.a_id=a.id
#     join janr as j on k.j_id=j.id
#     group by a.name,j.name
#     order by jami desc;