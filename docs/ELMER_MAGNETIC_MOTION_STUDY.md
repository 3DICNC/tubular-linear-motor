# Elmer magnetic motion study

This folder records the first axisymmetric Elmer magnetostatic motion study for the 10 mm magnet concept.

## Model

- 10 x 10 mm alternating axial permanent magnets
- 10 x 2 mm steel spacer buttons
- 5 mm wide coil region, 13 mm bore to 26 mm outside diameter
- Three coil positions across the fixed magnet stack

The permanent magnet material uses an axial magnetization of +/-820 kA/m. The field is solved by Elmer's `MagnetoDynamics2D` solver. The model outputs vector potential and magnetic flux density in VTU format.

## Results

`elmer_coil_motion_study.gif` combines the three solved positions. The steel-button region produces a local idealized peak of about 2.84 T; this is a finite-element local value and is not a value to use as a free-air field rating.

## Files

- `motion_left.sif`, `motion_center.sif`, `motion_right.sif`: Elmer solver inputs.
- `mesh_left`, `mesh_center`, `mesh_right`: solved VTU field data.
- `motion_left.png`, `motion_center.png`, `motion_right.png`: rendered field frames.
- `elmer_coil_motion_study.gif`: combined visual study.

This is a geometry and field-visualization study. It is not yet the final full-stroke, nine-coil force model.
