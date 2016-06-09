b1 = [4.8701906300747275;1.0456167830952363;2.1270254933250907;1.8245204740549978];
x = zeros(4,8);
x(1,:) = [-0.72381933160938616;1.8058137840101691;-1.6343100870318152;1.5637013510364555;-0.70656853381687945;1.9302449219664466;0.13867756647977664;0.36123371217955624];
x(2,:) = [-0.39898872031293725;-0.1383939503627149;0.65267899215862046;0.72758819747648606;1.8592383127858152;0.077354268082576255;-0.65639797448166026;-1.3788236706790626];
x(3,:) = [2.8038206853347631;-1.4226073538927584;7.0475072400200505;5.3165370362681266;12.02236855044843;1.7163652868707586;-1.9893585415872874;3.5725950020353148];
x(4,:) = [0.28815071921769203;-0.94191125864331349;0.65065003798376786;0.84316432346419001;0.67341341605309157;1.2903275321065355;0.41597307820357576;0.57180837959922448];
V = zeros(4,9);
V(:,1) = b1;
for i=1:4
    for j=2:9
        V(i,j) = x(i,j-1);
    end
end
W = [2.4344930638780173 -0.36655627805253377 -1.0791577943419153 -0.13742463204477007];

xlswrite('E:\IIT Roorkee\IOP (RTCoMU)\Training\weights.xlsx',V,1,'A1:I4');
xlswrite('E:\IIT Roorkee\IOP (RTCoMU)\Training\weights.xlsx',W,1,'A6:D6');