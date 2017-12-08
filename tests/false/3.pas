program Proc_Func

procedure procExample (b:boolean)
var mp : boolean;
begin
  b := false
  mp := not b
  writeBool(mp);
  writeLn()
end;

begin
    c := 'z';
    i := 13;
    j := 0;
    b := not false or (13 <> j);

    procExample();
    j := funcExample(false, i);
    writeInt(j);

    i := 70 + 80 * 5 + 3;
    i := 1 * 2 + 3 * 4
end.