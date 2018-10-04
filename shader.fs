varying vec2 vUv;
uniform float time;
uniform int shadingMode;
uniform sampler2D texture0;
varying vec3 lightPos, eyeVertex, eyeNormal;
varying vec4 diffuse;
varying float qAttenuation, cAttenuation, lAttenuation;

// this creates some wavy colo
vec4 showShading() {
    vec2 p = vUv;
    float a = time * 100.0;
    float d, e, f, g = 1.0 / 40.0 ,h ,i ,r ,q;
    e = 400.0 * ( p.x * 0.5 + 0.5 );
    f = 400.0 * ( p.y * 0.5 + 0.5 );
    i = 200.0 + sin( e * g + a / 150.0 ) * 20.0;
    d = 200.0 + cos( f * g / 2.0 ) * 18.0 + cos( e * g ) * 7.0;
    r = sqrt( pow( abs( i - e ), 2.0 ) + pow( abs( d - f ), 2.0 ) );
    q = f / r;
    e = ( r * cos( q ) ) - a / 2.0;
    f = ( r * sin( q ) ) - a / 2.0;
    d = sin( e * g ) * 176.0 + sin( e * g ) * 164.0 + r;
    h = ( ( f + d ) + a / 2.0 ) * g;
    i = cos( h + r * p.x / 1.3 ) * ( e + e + a ) + cos( q * g * 6.0 ) * ( r + h / 3.0 );
    h = sin( f * g ) * 144.0 - sin( e * g ) * 212.0 * p.x;
    h = ( h + ( f - e ) * q + sin( r - ( a + h ) / 7.0 ) * 10.0 + i / 4.0 ) * g;
    i += cos( h * 2.3 * sin( a / 350.0 - q ) ) * 184.0 * sin( q - ( r * 4.3 + a / 12.0 ) * g ) + tan( r * g + h ) * 184.0 * cos( r * g + h );
    i = mod( i / 5.6, 256.0 ) / 64.0;
    if ( i < 0.0 ) i += 4.0;
    if ( i >= 2.0 ) i = 4.0 - i;
    d = r / 350.0;
    d += sin( d * d * 8.0 ) * 0.52;
    f = ( sin( a * g ) + 1.0 ) / 2.0;
    return vec4( vec3( f * i / 1.6, i / 2.0 + d / 13.0, i ) * d * p.x + vec3( i / 1.3 + d / 8.0, i / 2.0 + d / 18.0, i ) * d * ( 1.0 - p.x ), 1.0 );
}

// calculate texture color based on the texture coordinates
vec4 showTexture() {
    float pos = sin(time);
    vec2 tex = vec2(gl_TexCoord[0].x * 0.5 + pos, (gl_TexCoord[0].y * 0.5) + 0.5);
    return texture2D(texture0, tex);
}

// per pixel lighting
vec3 lightingColor(vec3 inputColor) {
    float Len = length(lightPos - eyeVertex);
    vec3 lightVector = normalize(lightPos - eyeVertex);
    float NdotH = max(dot(eyeNormal, lightVector), 0.1);
    float attenuation = 1.0 / (qAttenuation * Len * Len + cAttenuation + Len * lAttenuation);
    return inputColor * attenuation * NdotH;
}

// main loop, calculate the shading differently depending on the mode
void main() {
    vec4 finalColor = vec4(0.0, 0.0, 0.0, 1.0); 
    
    if (shadingMode == 1)
    {
        finalColor = showTexture();
    }
    else if (shadingMode == 0)
    {
        finalColor = showShading();
    }
    else
    {
        finalColor = showTexture() + showShading() / 2.0;
    }
    
    gl_FragColor = vec4(lightingColor(vec3(finalColor)), 1.0);
}
