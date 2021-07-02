unit dmnfe;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Dialogs, ACBrNFe, ACBrCTe, ACBrCTeDACTeRLClass, ACBrNFeDANFeRLClass;

type

  { TNFeDM }

  TNFeDM = class(TDataModule)
    ACBrCTe1: TACBrCTe;
    ACBrCTeDACTeRL1: TACBrCTeDACTeRL;
    ACBrNFe1: TACBrNFe;
    ACBrNFeDANFeRL1: TACBrNFeDANFeRL;
  private

  public

  end;

  function setPdfPath(path: PChar): Integer; cdecl;
  function nfePdf(xml: PChar): Integer; cdecl;
  function nfeEventoPdf(xml: PChar): Integer; cdecl;
  function ctePdf(xml: PChar): Integer; cdecl;

var
  NFeDM: TNFeDM;
  dm: TNFeDM;
  pathPdf: string;

implementation

{$R *.lfm}

function setPdfPath(path: PChar): Integer; cdecl;
begin
  pathPdf:=path;
  Result:=1;
end;

function nfePdf(xml: PChar): Integer; cdecl;
begin
  try
    dm.ACBrNFe1.NotasFiscais.LoadFromString(xml);
    dm.ACBrNFeDANFeRL1.PathPDF:=pathPdf;
    dm.ACBrNFe1.NotasFiscais.ImprimirPDF;
  finally
    dm.ACBrNFe1.NotasFiscais.Clear;
  end;
  Result:=1;
end;

function nfeEventoPdf(xml: PChar): Integer; cdecl;
begin
  try
    dm.ACBrNFe1.EventoNFe.LerXMLFromString(xml);
    dm.ACBrNFeDANFeRL1.PathPDF:=pathPdf;
    dm.ACBrNFe1.ImprimirEventoPDF;
  finally
    dm.ACBrNFe1.NotasFiscais.Clear;
  end;
  Result:=1;
end;

function ctePdf(xml: PChar): Integer; cdecl;
begin
  try
    dm.ACBrCTe1.Conhecimentos.LoadFromString(xml);
    dm.ACBrCTeDACTeRL1.PathPDF:=pathPdf;
    dm.ACBrCTe1.Conhecimentos.ImprimirPDF;
  finally
    dm.ACBrCTe1.Conhecimentos.Clear;
  end;
  Result:=1;
end;

initialization
  dm:=TNFeDM.Create(nil);

end.

