// Rev64: 0.5 mm bobbin wall. Units mm; motor axis Z.
// STEP exports contain exact solids. Lands/end flanges remain provisional.
/* [Display] */
part="assembly"; // [assembly,bobbin,coils,stack,tube,magnet,pole,reference]
cutaway=false;
position=0; // [-20:0.25:20]
show_reference=false;
/* [Winding pack] */
coil_count=6;
coil_pitch=8;
coil_width=4;
bobbin_id=12.4;
bobbin_wall=0.5;
coil_od=16.8;
end_flange=0.5;
/* [Stationary stack] */
magnet_od=10;
magnet_piece_length=5;
magnet_pairs=8;
pole_id=5;
pole_width=2;
tube_id=10.2;
tube_od=12;
/* [Reference envelope, no assigned material] */
reference_id=17;
reference_od=23;
/* [Hidden] */
$fn=192;
coil_id=bobbin_id+2*bobbin_wall;
stack_length=magnet_pairs*2*magnet_piece_length+(magnet_pairs-1)*pole_width;
pack_length=(coil_count-1)*coil_pitch+coil_width;
centres=[for(i=[0:coil_count-1]) (i-(coil_count-1)/2)*coil_pitch];
phase_colors=[[0.87,0.47,0.17],[0.75,0.36,0.10],[0.95,0.62,0.25]];
assert(bobbin_id>tube_od && bobbin_wall>0);
assert(coil_pitch>=coil_width && coil_od>coil_id);
assert(abs(position)+pack_length/2+end_flange<=stack_length/2,"Former exceeds stack length");
module ring(id,od,z,h) {
    translate([0,0,z]) difference() {
        cylinder(d=od,h=h);
        if(id>0) translate([0,0,-0.01]) cylinder(d=id,h=h+0.02);
    }
}
module former() {
    union() {
        ring(bobbin_id,coil_id,-pack_length/2-end_flange,pack_length+2*end_flange);
        ring(bobbin_id,coil_od,-pack_length/2-end_flange,end_flange);
        for(i=[0:coil_count-2]) ring(bobbin_id,coil_od,centres[i]+coil_width/2,coil_pitch-coil_width);
        ring(bobbin_id,coil_od,pack_length/2,end_flange);
    }
}
module winding_pack() {
    for(i=[0:coil_count-1]) color(phase_colors[i%3])
        ring(coil_id,coil_od,centres[i]-coil_width/2,coil_width);
}
module magnetic_stack() {
    for(i=[0:magnet_pairs-1]) {
        z=-stack_length/2+i*(2*magnet_piece_length+pole_width);
        for(j=[0:1]) color(i%2==0?[0.72,0.24,0.26]:[0.20,0.43,0.72])
            ring(0,magnet_od,z+j*magnet_piece_length,magnet_piece_length);
        if(i<magnet_pairs-1) color([0.62,0.66,0.70])
            ring(pole_id,magnet_od,z+2*magnet_piece_length,pole_width);
    }
}
module selected_model() {
    if(part=="assembly" || part=="stack") magnetic_stack();
    if(part=="assembly" || part=="tube") color([0.20,0.24,0.28]) ring(tube_id,tube_od,-stack_length/2,stack_length);
    if(part=="assembly" || part=="coils") translate([0,0,position]) winding_pack();
    if(part=="assembly" || part=="bobbin") translate([0,0,position]) color([0.85,0.82,0.65]) former();
    if(part=="magnet") ring(0,magnet_od,0,magnet_piece_length);
    if(part=="pole") ring(pole_id,magnet_od,0,pole_width);
    if(part=="reference") ring(reference_id,reference_od,-stack_length/2,stack_length);
}
difference() {
    selected_model();
    if(cutaway) translate([-reference_od,0,-stack_length]) cube([2*reference_od,reference_od,2*stack_length]);
}
if(show_reference && part=="assembly") %ring(reference_id,reference_od,-stack_length/2,stack_length);
