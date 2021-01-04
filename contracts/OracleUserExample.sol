import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

import "contracts/ParalinkOracle.sol";

pragma solidity 0.6.12;

contract OracleUserExample is Ownable {
    using SafeMath for uint256;
    using Address for address;

    ParalinkOracle oracle;

    bytes32 public someData;

    constructor(address paralinkOracle) public Ownable() {
        oracle = ParalinkOracle(paralinkOracle);
    }

    function initiateRequest(bytes32 _ipfsHash, uint256 _nonce)
        public
        onlyOwner
    {
        bytes4 callbackFunctionId = bytes4(
            keccak256("callbackFunction(bytes32)")
        );
        oracle.request(
            _ipfsHash,
            msg.sender,
            address(this),
            callbackFunctionId,
            _nonce,
            ""
        );
    }

    function callbackFunction(bytes32 _data) public {
        require(
            msg.sender == address(oracle) || msg.sender == owner(),
            "Invalid permissions."
        );

        someData = _data;
    }
}