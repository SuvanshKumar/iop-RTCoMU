V = xlsread('E:\IIT Roorkee\IOP (RTCoMU)\Training\weights.xlsx','A1:I4');
W = xlsread('E:\IIT Roorkee\IOP (RTCoMU)\Training\weights.xlsx','A6:D6');
X = [1;0.742943548;0.599798387;0.714415323;0.038120996;1.533285774;18.54989919;7.399727812;0.949799265];

Y = V*X;
for i=1:4
    Y(i) = (1-exp(-2*Y(i)))/(1+exp(-Y(i)));
end
Z = W*Y;
