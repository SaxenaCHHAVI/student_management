CREATE TABLE test.STUDENT (
    name varchar(30),
    class varchar(30),
    roll varchar(30),
    address varchar(30),
    phone varchar(30)
);
Select * from test.student;

Create table test.Fee_Structure (
    class varchar(30),
    amount varchar(30)
);
select * from test.FEE_STRUCTURE;

insert into test.FEE_STRUCTURE values ('1', '3000');
insert into test.FEE_STRUCTURE values ('2', '3500');
insert into test.FEE_STRUCTURE values ('3', '4000');
insert into test.FEE_STRUCTURE values ('4', '4500');
insert into test.FEE_STRUCTURE values ('5', '5000');
insert into test.FEE_STRUCTURE values ('6', '5500');
insert into test.FEE_STRUCTURE values ('7', '6000');
insert into test.FEE_STRUCTURE values ('8', '6500');
insert into test.FEE_STRUCTURE values ('9', '7000');
insert into test.FEE_STRUCTURE values ('10', '7500');
insert into test.FEE_STRUCTURE values ('11', '8000');
insert into test.FEE_STRUCTURE values ('12', '8500');
commit;
