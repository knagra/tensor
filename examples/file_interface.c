/* A new interface for the LED Grid.  At every new frame, the pixel_color function below
 * will call another function, generate_board, that will store the contents of the board
 * in a file; the format for storage by generate_board will be in the form of lines, with
 * the first line indicating the red values for all the pixels in the first row, with the
 * index at the bottom left.  So, the board will be the upper right quadrant of the plane
 * in mathematics.  That is, the pixel (0, 0) is the bottom left corner pixel of the
 * board as seen by a viewer.  The next line will be the green values for the first row,
 * the next line the blue values, the next the red values for the second row, and so on.
 * Then this function will grab the information from the file in which the function
 * generate_board stores the values.
 */

unsigned char pixel_color(int x, int y, int frame, int color) {
  
}
