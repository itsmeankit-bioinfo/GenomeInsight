from genomeinsight.analysis.protein import (
    analyze_protein,
    amino_acid_composition,
    aromaticity,
    gravy,
    instability_index,
    isoelectric_point,
    molecular_weight,

)


SEQUENCE = "MKWVTFISLLFLFSSAYSRGVFRR"


def test_analyze_protein():
    result = analyze_protein(SEQUENCE)

    assert result["length"] == len(SEQUENCE)
    assert result["molecular_weight"] > 0
    assert result["isoelectric_point"] > 0


def test_amino_acid_composition():
    composition = amino_acid_composition(SEQUENCE)

    assert composition["M"] == 1
    assert sum(composition.values()) == len(SEQUENCE)


def test_molecular_weight():
    assert molecular_weight(SEQUENCE) > 0


def test_isoelectric_point():
    assert isoelectric_point(SEQUENCE) > 0


def test_gravy():
    assert isinstance(gravy(SEQUENCE), float)


def test_aromaticity():
    assert isinstance(aromaticity(SEQUENCE), float)


def test_instability():
    assert isinstance(instability_index(SEQUENCE), float)

def test_molecular_weight_units():
    mw = molecular_weight(SEQUENCE)

    assert mw > 0
    assert mw / 1000 > 0

def test_pi_function():
    assert isoelectric_point(SEQUENCE) > 0

def test_pi():
    assert isoelectric_point(SEQUENCE) > 0
