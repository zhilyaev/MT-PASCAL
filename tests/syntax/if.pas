program my;
var i: integer;
begin

  if true then
    i:=5
  else i:=3;

  if true then
  begin
    i:=5;
  end
  else i:=3;

  if true then
  begin
    i:=5
  end
  else if false then i:=3;

  if true then
  begin
    i:=5
  end
  else if false then i:=3
  else i:=0

end.