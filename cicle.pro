a = indgen(3,3)
print,a
print,'   '

FOR j=0,2 DO BEGIN 
	FOR i=0,2 DO BEGIN
		number = a[i,j]
		lable1: 

		if number gt 1 then begin
			number = number - 2
			GOTO, lable1 
			end else begin
				if number eq 0 then print,i+1,',',j+1
			
		endelse
		
	ENDFOR
ENDFOR
end
