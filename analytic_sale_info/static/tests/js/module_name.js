/* Copyright 2025 Moduon Team S.L.
 * License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0) */

odoo.define_section("module_name", ["module_name.ExportedObject"], function (test) {
    "use strict";

    test("It should demonstrate a PhantomJS test for web (backend)", function (assert, ExportedObject) {
        var expect = "Expected Return",
            result = new ExportedObject();
        assert.assertStrictEqual(
            result,
            expect,
            "Result !== Expect and the test failed with this message"
        );
    });
});
