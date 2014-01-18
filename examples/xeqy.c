unsigned char pixel_color(int x, int y, int frame, int color) {
  if (x == y) {
    return 0xF;
  } else {
    return 0x0;
  }
}
