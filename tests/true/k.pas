program p;
procedure f1(a:boolean);
var z:character;
begin
z:='a';
if a then z:=z+1
else z:=z-1;
end;
begin
f1(false);
end.