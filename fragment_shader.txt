varying vec3 vN;
varying vec3 v; 
varying vec4 color;
#define MAX_LIGHTS 1 
void main (void) 
{ 
   vec3 N = normalize(vN);
   vec4 finalColor = vec4(0.0, 0.0, 0.0, 0.0);
   
   for (int i=0;i<MAX_LIGHTS;i++)
   {
      vec3 L = normalize(gl_LightSource[i].position.xyz - v); 
      vec3 E = normalize(-v); // we are in Eye Coordinates, so EyePos is (0,0,0) 
      vec3 R = normalize(-reflect(L,N)); 
   
      vec4 Iamb = gl_LightSource[i].ambient; 
      vec4 Idiff = gl_LightSource[i].diffuse * max(dot(N,L), 0.0);
      Idiff = clamp(Idiff, 0.0, 1.0); 
      vec4 Ispec = gl_LightSource[i].specular * pow(max(dot(R,E),0.0),0.3*gl_FrontMaterial.shininess);
      Ispec = clamp(Ispec, 0.0, 1.0); 
   
      finalColor += Iamb + Idiff + Ispec;
   }
   gl_FragColor = color * finalColor; 
}