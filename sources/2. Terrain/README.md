Terrain guide

After you have your concept put togehter, make the landscape in blender.
I used the A.N.T. landscape plugin - messed around until i got something resembling rolling hills
Make the camera be orthogonal and perfect exponent of two (2048x2048 pixles for instance)
Make the therrain height mapped (see nodes of the material) and render it to a texture
save_as the texture for import in sandbox (it will be PNG)
Conver the texture to BMP (easy) or PGM (ascii format better but tricky)
Import the terain into sandbox2 editor and play with it until you have the proper size and height
see the very rudimentary converter.py3 made for tuning the height with python (examine the source)
Try have fun :o}
To get all the assets open the asset DB manager and add the libraries you map will depend on...

Now that you have the barren contour of the terrain you can assign the material kinds and types.
Define the angles and heights for the terrain to make painting the terrain easier,
Paint the terrain.

You now have the barren basic terrain on the map ready to receive game assets.
