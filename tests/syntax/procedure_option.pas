program my;


procedure single( i : boolean );
var k: integer;
begin
  i:=true;
end;

procedure double(i:integer; k:integer);

begin
  i:=5;
  k:=0;
end;


begin
  single(true);
  double(1,4);
end.