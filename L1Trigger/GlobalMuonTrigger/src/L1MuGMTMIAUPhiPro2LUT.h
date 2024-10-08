//-------------------------------------------------
//
/** \class L1MuGMTMIAUPhiPro2LUT
 *
 *   MIAUPhiPro2 look-up table
 *          
 *   this class was automatically generated by 
 *     L1MuGMTLUT::MakeSubClass()  
*/
//
//   Author :
//   H. Sakulin            HEPHY Vienna
//
//   Migrated to CMSSW:
//   I. Mikulec
//
//--------------------------------------------------
#ifndef L1TriggerGlobalMuonTrigger_L1MuGMTMIAUPhiPro2LUT_h
#define L1TriggerGlobalMuonTrigger_L1MuGMTMIAUPhiPro2LUT_h

//---------------
// C++ Headers --
//---------------

//----------------------
// Base Class Headers --
//----------------------
#include "L1Trigger/GlobalMuonTrigger/src/L1MuGMTLUT.h"

//------------------------------------
// Collaborating Class Declarations --
//------------------------------------

//              ---------------------
//              -- Class Interface --
//              ---------------------

class L1MuGMTMIAUPhiPro2LUT : public L1MuGMTLUT {
public:
  enum { MIP_DT, MIP_BRPC, ISO_DT, ISO_BRPC, MIP_CSC, MIP_FRPC, ISO_CSC, ISO_FRPC };

  /// constuctor using function-lookup
  L1MuGMTMIAUPhiPro2LUT()
      : L1MuGMTLUT("MIAUPhiPro2",
                   "MIP_DT MIP_BRPC ISO_DT ISO_BRPC MIP_CSC MIP_FRPC ISO_CSC ISO_FRPC",
                   "cphi_start(5) cphi_fine(1) cphi_ofs(3) charge(1)",
                   "phi_sel(18)",
                   11,
                   false) {
    InitParameters();
  };

  /// destructor
  ~L1MuGMTMIAUPhiPro2LUT() override {}

  /// specific lookup function for phi_sel
  unsigned SpecificLookup_phi_sel(
      int idx, unsigned cphi_start, unsigned cphi_fine, unsigned cphi_ofs, unsigned charge) const {
    std::vector<unsigned> addr(4);
    addr[0] = cphi_start;
    addr[1] = cphi_fine;
    addr[2] = cphi_ofs;
    addr[3] = charge;
    return Lookup(idx, addr)[0];
  };

  /// specific lookup function for entire output field
  unsigned SpecificLookup(int idx, unsigned cphi_start, unsigned cphi_fine, unsigned cphi_ofs, unsigned charge) const {
    std::vector<unsigned> addr(4);
    addr[0] = cphi_start;
    addr[1] = cphi_fine;
    addr[2] = cphi_ofs;
    addr[3] = charge;
    return LookupPacked(idx, addr);
  };

  /// access to lookup function with packed input and output

  unsigned LookupFunctionPacked(int idx, unsigned address) const override {
    std::vector<unsigned> addr = u2vec(address, m_Inputs);
    return TheLookupFunction(idx, addr[0], addr[1], addr[2], addr[3]);
  };

private:
  /// Initialize scales, configuration parameters, alignment constants, ...
  void InitParameters();

  /// The lookup function - here the functionality of the LUT is implemented
  unsigned TheLookupFunction(int idx, unsigned cphi_start, unsigned cphi_fine, unsigned cphi_ofs, unsigned charge) const;

  /// Private data members (LUT parameters);
  int m_IsolationCellSizePhi;
};
#endif
