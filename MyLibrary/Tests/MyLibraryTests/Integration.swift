import XCTest
@testable import MyLibrary

final class IntegerationTests: XCTestCase {

    func testTempInteger() async throws {
        // Given
        let service_obj = WeatherServiceImpl()

        // When
        let tp = try await service_obj.getTemperature()

        // Then
        XCTAssertNotNil(tp)
        //Checking if the temp is integer
        XCTAssert((tp as Any) is Int)

    }

}