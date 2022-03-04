/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const listProfile = /* GraphQL */ `
  query ListProfile {
    listProfile {
      nombre
      razonsocial
      rfc
      direccion
      telefono
    }
  }
`;
export const getProfile = /* GraphQL */ `
  query GetProfile($rfc: String!) {
    getProfile(rfc: $rfc) {
      nombre
      razonsocial
      rfc
      direccion
      telefono
    }
  }
`;
